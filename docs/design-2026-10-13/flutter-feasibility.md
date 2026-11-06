# Flutter feasibility: a premium, glass-heavy, motion-rich MockMob app on the Galaxy M06

Date: 13 October 2026. Scope: technical feasibility only (no visual direction). Nothing was built or installed for this note.
Toolchain checked in the repo: Flutter 3.44.6 stable (engine d3a3293, July 2026), Riverpod 3, go_router 17.5, Impeller.

**Verdict.** The premium direction is feasible on the M06 if we treat glass as a scarce, budgeted resource rather than a material you put on everything. Three rules carry most of it:

1. **Real backdrop blur only on chrome that floats over content we don't control.** That means the tab dock, sheets and at most one sticky header, all under one `BackdropGroup`.
2. **Fake glass everywhere else.** Most "glass" in this app sits over our own atmosphere art, and we can paint a pre-blurred copy of that art for almost nothing.
3. **Animate with transforms, springs and pre-rendered art.** Full-screen shaders, live refraction and a native vector runtime each have to earn their place in an on-device benchmark first (section 12).

How certain each part is:

- **Verified from source or official docs:** the Mali-G57 runs Impeller on Vulkan, and Mali is not on the bad-driver list. Also verified: `BackdropGroup`, `ImageFilter.shader`, the `SpringDescription.withDurationAndBounce` API and the new haptic notification API.
- **Not measured yet:** every frame-time figure below is a target. None has been measured on the phone.

---

## 1. The device floor, in numbers that matter

| Fact | Value | Source / how to confirm |
|---|---|---|
| SoC / GPU | MediaTek Dimensity 6300 (2x A76 2.4 GHz + 6x A55), **Mali-G57 MC2** (2 shader cores, tile-based) | Spec listings (91mobiles, Smartprix) |
| Display | 6.7" PLS LCD, 720x1600, **90 Hz** per listings | Confirm on device: `adb shell dumpsys display \| grep -iE "refreshRate\|mode"`. Samsung "Motion smoothness" (Adaptive vs Standard) and power saving can cap it at 60 Hz |
| Density | ~300 dpi, so devicePixelRatio is about 1.875 and the logical width about 384 dp. Flutter picks `2.0x` assets | `adb shell wm density` |
| RAM | 4 GB SKU (3.5 GB visible), LPDDR4X | Owner's handover |
| Renderer | **Impeller on Vulkan.** In engine `driver_info_vk.cc`, `IsKnownBadDriver()` blocks Adreno <= 650, Huawei/Maleoon, Samsung Xclipse < Vulkan 1.3 and old PowerVR. **No Mali entry**, and G57 is in `kMaliVersions` | `adb logcat -s flutter` at launch shows the Impeller backend line. Compare `--no-enable-impeller` only for triage (the opt-out is deprecated) |
| Frame budget | **11.1 ms at 90 Hz** (16.7 ms at 60 Hz) for each of the UI thread and the raster thread | |

What "tile-based Mali with 2 cores" means for us:

- **Render-pass breaks are costly.** Each `BackdropFilter` or `saveLayer` forces the GPU to flush the tile memory and read the frame back. That costs far more than the blur maths itself.
- **Fill rate is the limit.** Full-screen per-pixel work (a shader background, a full-screen blur, stacked translucent layers) is what will drop us below 90 Hz. Widget count is not the problem.
- **Group and clip what must be live.** The fixes are: fewer live backdrops, smaller blurred areas, one shared backdrop per screen, and pre-rendering anything that does not change.

---

## 2. Glass: what it costs and how to do it

### 2.1 BackdropFilter under Impeller (Android Vulkan; the GLES fallback is not our device)

**Impeller history:**
- Flutter 3.19 removed an unnecessary onscreen-texture read. That made scenes with multiple backdrops 20-70% faster.
- Flutter 3.22 reimplemented the blur and roughly halved its CPU and GPU cost.
- Flutter 3.29 added `BackdropGroup` and `BackdropFilter.grouped`. Filters in a group share one backdrop snapshot, and identical filters can be fused (engine PR #55701).

**Cost model.** These are working rules, not measurements:
- **Fixed cost:** each live backdrop region pays a render-pass break plus a downsample, blur and upsample of the area under it.
- **Sigma:** Impeller downsamples harder as sigma grows. A larger sigma is therefore not much more expensive. Area and count are the real drivers.
- **Clip it.** A `BackdropFilter` without a clip filters the whole parent clip area, often the full screen. Always clip.
- **It re-renders every frame:** when anything behind it moves (scrolling content, animated background), the blur runs again on every frame. A static backdrop does not stop that cost.

**Pattern to adopt.** Wrap the shell body in one group. Every chrome glass uses the grouped constructor, clipped to its shape:

```dart
// app_shell.dart (new): content runs under a floating dock.
BackdropGroup(
  child: Stack(children: [
    Positioned.fill(child: shell),                 // tab branches; lists pad bottom by dock height + inset
    Align(alignment: Alignment.bottomCenter, child: const GlassDock()),
  ]),
)

// core/glass/glass_surface.dart
class GlassSurface extends StatelessWidget {
  const GlassSurface({super.key, required this.child, required this.radius, this.role = GlassRole.chrome});
  final Widget child; final double radius; final GlassRole role;

  @override
  Widget build(BuildContext context) {
    final q = GlassQuality.of(context);                 // full | lite | off (section 2.6)
    final g = context.glassTokens;                     // tint, edge light, sigma per role and theme
    final br = BorderRadius.circular(radius);
    Widget s = DecoratedBox(
      decoration: ShapeDecoration(
        color: g.tint(role, q),                        // lite/off: higher opacity, so legibility holds without blur
        shape: RoundedSuperellipseBorder(borderRadius: br),
      ),
      child: CustomPaint(foregroundPainter: EdgeLightPainter(br, g.edge), child: child),
    );
    if (q == GlassQuality.full) {
      s = BackdropFilter.grouped(filter: ImageFilter.blur(sigmaX: g.sigma(role), sigmaY: g.sigma(role)), child: s);
    }
    return ClipRSuperellipse(borderRadius: br, child: s); // the clip bounds the blurred area
  }
}
```

**Notes:**
- **Tile mode:** leave `tileMode` at its default for backdrop blurs. `TileMode.decal` darkens the edges.
- **Edge light:** `EdgeLightPainter` (a 1 dp gradient stroke plus a top sheen) is static and cheap. It is our "liquid" look without a shader. CampusOS already has a tested version of this exact pattern (`C:\Users\atish\Desktop\CampusOS\lib\core\widgets\glass.dart`, `GlassQuality.full/lite`, a `_EdgeLightPainter`). Port it instead of reinventing it.
- **Limits of a group:** grouped filters all sample the same snapshot, so glass on top of glass will not show the glass underneath. Design around that: no stacked glass.
- **Text on glass:** every glass surface that carries text needs a minimum tint opacity. That keeps the contrast at 4.5:1 or better against the worst backdrop: dark ground about 0.62, paper ground about 0.72, both to be tuned. Run the contrast check against a white and a black backdrop.

### 2.2 Fake glass from a cached, pre-blurred backdrop (the main technique)

Most surfaces in the new design will sit over **our own atmosphere**: gradient blobs, generated art, a brand texture. We know those pixels, so we never need to read the framebuffer back.

**How it works:**
1. Render the atmosphere once at **quarter resolution** (180x400 px on the M06). Atmosphere art is low-frequency, so nobody can see the difference.
2. Make a blurred copy once.
3. Each glass card draws the matching slice of the blurred copy behind itself with `drawImageRect`. That is a plain textured quad: no render-pass break, no blur per frame.

```dart
class AtmosphereCache {
  ui.Image? sharp, frosted;
  Future<void> prepare(Size logical, double dpr, void Function(Canvas, Size) paintArt) async {
    final w = (logical.width * dpr / 4).round(), h = (logical.height * dpr / 4).round();
    final r1 = ui.PictureRecorder(); paintArt(Canvas(r1), Size(w.toDouble(), h.toDouble()));
    sharp = await r1.endRecording().toImage(w, h);
    final r2 = ui.PictureRecorder();
    Canvas(r2).drawImage(sharp!, Offset.zero, Paint()..imageFilter = ui.ImageFilter.blur(sigmaX: 5, sigmaY: 5));
    frosted = await r2.endRecording().toImage(w, h);   // 180x400x4 bytes = 288 KB of GPU memory
  }
}

/// Paints the frosted slice of the atmosphere that sits behind this box. Repaints on scroll,
/// because list items sit behind their own RepaintBoundary and would otherwise keep a stale slice.
class RenderFakeGlass extends RenderProxyBox {
  RenderFakeGlass(this.cache, this.scroll, this.screenSize);
  final AtmosphereCache cache; final Listenable? scroll;
  Size screenSize;   // logical screen size; updated from MediaQuery in updateRenderObject
  @override void attach(PipelineOwner o) { super.attach(o); scroll?.addListener(markNeedsPaint); }
  @override void detach() { scroll?.removeListener(markNeedsPaint); super.detach(); }
  @override
  void paint(PaintingContext context, Offset offset) {
    final img = cache.frosted;
    if (img != null) {
      final g = localToGlobal(Offset.zero);
      final sx = img.width / screenSize.width, sy = img.height / screenSize.height;
      final src = Rect.fromLTWH(g.dx * sx, g.dy * sy, size.width * sx, size.height * sy);
      context.canvas.drawImageRect(img, src, offset & size, Paint()..filterQuality = FilterQuality.low);
    }
    super.paint(context, offset);   // the tint, the edge light and the content on top
  }
}
```

**Limits:**
- **Static art only.** If the atmosphere animates, the frosted copy goes stale. Either animate the fake glass with the same transform (blobs drifting by `t` can be drawn twice, once sharp and once pre-blurred) or keep the drift tiny.
- **No content behind it.** Fake glass does not show other content behind it. Content scrolling under the dock still needs the real `BackdropFilter`. That is the split: dock and sheets real, cards fake.
- **The package equivalent** is `liquid_glass_renderer`'s `FakeGlass`. It still uses a backdrop filter, so it is cheaper than its refraction but not free. The cache above is cheaper still.

### 2.3 Liquid glass (refraction, specular edges) with shaders

- **The engine primitive:** `BackdropFilter(filter: ImageFilter.shader(fragmentShader))`. It is **Impeller only**, so check `ui.ImageFilter.isShaderFilterSupported` and fall back. Uniform rules:
  - The first uniform must be a `vec2` size, which the engine sets.
  - The first `sampler2D` receives the backdrop.
  - The GLES backend flips y (`#ifdef IMPELLER_TARGET_OPENGLES`).
  - Flutter 3.44 also binds uniforms by name (`shader.getUniformFloat('uName')`) and warns about shaders that will not work under Skia.
- **Use it once, small: the dock's selection lens.** A 64x40 dp lens that refracts the icons under it costs about 140x75 px of fragment work, which is trivial. A full-width refractive dock costs about 6x more and adds the render-pass break. Benchmark before choosing.

  ```glsl
  #include <flutter/runtime_effect.glsl>
  uniform vec2 uSize;          // set by the engine
  uniform float uRadius;       // corner radius in px
  uniform float uStrength;     // refraction, e.g. 0.06
  uniform sampler2D uBackdrop; // set by the engine
  out vec4 fragColor;
  float sdRoundBox(vec2 p, vec2 b, float r) { vec2 q = abs(p) - b + r; return length(max(q, 0.)) + min(max(q.x, q.y), 0.) - r; }
  void main() {
    vec2 uv = FlutterFragCoord().xy / uSize;
  #ifdef IMPELLER_TARGET_OPENGLES
    uv.y = 1.0 - uv.y;
  #endif
    vec2 p = (uv - 0.5) * uSize;
    float d = sdRoundBox(p, uSize * 0.5, uRadius);
    float edge = smoothstep(-14.0, 0.0, d);                        // 0 inside, 1 near the rim
    vec2 n = normalize(p + 1e-4);
    vec2 refr = uv - n * edge * edge * uStrength;                  // bend toward the centre near the rim
    vec4 c = texture(uBackdrop, refr);
    float spec = pow(clamp(dot(n, normalize(vec2(-0.4, -1.0))), 0., 1.), 8.) * edge;  // top-left highlight
    fragColor = c + vec4(vec3(spec * 0.35), 0.0);
  }
  ```
  Load it once at splash with `FragmentProgram.fromAsset('shaders/lens.frag')` (declared under `flutter: shaders:`), and reuse one `FragmentShader` across frames. Impeller compiles shaders ahead of time, but the Vulkan pipeline is still created on first use. **Draw the lens once offscreen during splash** so the first tab switch does not hitch.
- **Package option: `liquid_glass_renderer`** (whynotmake-it).
  - **Status:** latest 0.2.0-dev.4, **pre-release, last published about 11 months ago**. 889 likes. Impeller only (iOS, Android, macOS).
  - **Documented limits:** "experimental, do not add blindly to production"; **memory spikes while animating shapes** (a Flutter texture-disposal bug); at most 16 shapes per `LiquidGlassBlendGroup`; blur artifacts when shapes blend.
  - **Good ideas worth copying:** `LiquidStretch` (squash on drag), `GlassGlow` (a touch-follow highlight), `LiquidGlassLayer(fake: true)`.
  - **Recommendation:** use it as a **reference and a benchmark subject**, not a dependency. If the dock benchmark (B5) is clean on the M06, vendoring its dock shader is acceptable. Otherwise use our own lens shader or the edge-light painter.

### 2.4 When to use which glass

| Surface | Over what | Technique on M06 |
|---|---|---|
| Tab dock | Scrolling content | Real `BackdropFilter.grouped`, sigma 16-24, plus the edge light. The selection lens is either a shader (if B6 passes) or tint plus edge light |
| Bottom sheets, menus | Any screen | Real blur, grouped. Only one sheet is ever open |
| Sticky large-title header | Scrolling content | Real blur **only if B3 passes with dock + header**. Otherwise an opaque header that fades in |
| Cards, hero panels, onboarding panels | Our atmosphere | **Fake glass** (2.2) |
| Runner (question and options), repair, result numbers | Anything | **No glass.** Solid surfaces. Reading and answering must stay calm and legible |

### 2.5 Other Impeller habits for this GPU

- **Avoid big translucent layers.** `Opacity`, `ShaderMask`, `ColorFiltered` and `saveLayer` all force offscreen passes. Prefer `FadeTransition` or `AnimatedOpacity` on small subtrees; Impeller can fold opacity into a single draw. Never put an `Opacity` or `ShaderMask` on a whole page. `lib/features/learn/widgets/reveal_in.dart` uses `Opacity` in a builder; switch it to `FadeTransition`.
- **Shadows on rounded rects are cheap; on paths they are not.** Impeller draws blurred rounded-rect shadows analytically. Shadows on arbitrary paths, or `BoxShadow`s on non-rect shapes, become real blurs.
- **Gradient banding on the LCD.** A dark mesh gradient on an 8-bit LCD bands. Impeller dithers gradients, but pre-rendered WebP art should have about 2% grain baked in.
- **Clip to the shape you draw.** Prefer `ClipRSuperellipse` / `RoundedSuperellipseBorder`. Avoid `Clip.antiAliasWithSaveLayer`.
- **No glass over platform views** (Custom Tabs and sign-in are separate activities, so this is fine today).

### 2.6 Adaptive quality

Android exposes no "reduce transparency" setting to apps. One UI has one in Accessibility, but it is not readable through Flutter. So we ship:

- **A user setting:** You > Appearance > Glass: **Full / Lite / Off**. *Lite* means fake glass everywhere and real blur only on sheets. *Off* means opaque tints. Default to Full on the M06 if the benchmarks pass, otherwise Lite.
- **An automatic drop.** Watch frame timings and step Full down to Lite once per install when the raster thread keeps missing the budget during interaction:

```dart
SchedulerBinding.instance.addTimingsCallback((List<FrameTiming> ts) {
  for (final t in ts) { _raster.add(t.rasterDuration.inMicroseconds); }  // ring buffer of 180
  if (_raster.length == 180 && _raster.p90 > 0.9 * budgetMicros) {       // budget = 1e6 / refresh rate
    ref.read(glassQualityProvider.notifier).downgrade(reason: 'p90 raster');  // persisted, logged to analytics
  }
});
```

- **Reduced motion** (`Motion.reduced`) stops atmosphere drift and lens motion, but keeps static glass.

---

## 3. Floating glass tab bar

**Shape:**
- A pill dock, inset 12 dp from the sides and 8 dp above the gesture inset, about 64 dp tall.
- Five 48 dp or larger targets, with labels kept (the five tabs are product nouns, so they stay as words).
- Content scrolls underneath. Every tab root adds `bottom: dockHeight + inset + 16` of padding through one `DockInsets` inherited widget.

**Indicator:** a lens or pill moved by a **spring**. It stretches with velocity, so it feels liquid without any shader:

```dart
class _DockState extends State<GlassDock> with SingleTickerProviderStateMixin {
  late final AnimationController _x = AnimationController.unbounded(vsync: this, value: widget.index.toDouble());
  static final _spring = SpringDescription.withDurationAndBounce(duration: const Duration(milliseconds: 380), bounce: 0.18);

  void _goTo(int i, {double velocity = 0}) {
    if (Motion.reduced(context)) { _x.value = i.toDouble(); return; }
    _x.animateWith(SpringSimulation(_spring, _x.value, i.toDouble(), velocity));  // interruptible; keeps velocity
  }

  // Drag across the dock to scrub tabs (iOS 26 / One UI style): tick on every boundary crossed.
  void _onDrag(DragUpdateDetails d) {
    final prev = _x.value.round();
    _x.value = (_x.value + d.delta.dx / _slot).clamp(0, 4);
    if (_x.value.round() != prev) ref.read(hapticsProvider).tick();
  }
  void _onDragEnd(DragEndDetails d) {
    final target = _x.value.round();
    _goTo(target, velocity: d.velocity.pixelsPerSecond.dx / _slot);
    widget.onTap(target);
  }

  Widget _lens() => AnimatedBuilder(
    animation: _x,
    builder: (_, child) {
      final stretch = 1 + (_x.velocity.abs() * 0.035).clamp(0.0, 0.22);           // squash-and-stretch
      return Transform(
        transform: Matrix4.translationValues(_x.value * _slot, 0, 0)..scale(stretch, 2 - stretch, 1),
        alignment: Alignment.center,
        child: child,
      );
    },
    child: const RepaintBoundary(child: DockLens()),   // tint + edge light, or the lens shader
  );
}
```

**Details:**
- **Icons:** cross-fade outline to filled (Lucide 300 to 400, as today) and scale 0.92 to 1 on a spring. The active label goes ink, inactive ones ink3.
- **Press:** pressing an item scales it to 0.94 and brightens the edge light (a `pressed` flag, as in CampusOS).
- **Haptics:** `selectionClick` on each tab change and drag crossing. Nothing on a re-tap, which keeps the existing scroll-to-top behaviour.
- **Scroll behaviour (optional):** the dock shrinks to about 0.9 scale while you scroll down (transform only) and returns on scroll up or idle. Never hide it entirely; five tabs is the core navigation.
- **Accessibility:** keep the current `Semantics(button, selected, label: "Practice, tab 2 of 5")` and the Review dot semantics. Drag-scrub is an extra; taps still work.
- **Performance:** the dock is the **one always-on live blur**. Measure it in B2.

---

## 4. Transitions, Hero and go_router

- **The Hero limit in our router.** A Hero flies only between routes on the **same Navigator**. go_router gives each `StatefulShellBranch` its own Navigator (each with its own `HeroControllerScope`). In `router.dart` most destinations push on the **root** navigator: result, runner, repair, learn run and weekly ending. So a Hero from a Today or Practice card to those screens **will not fly**. Two options:
  1. **Same-navigator Hero.** For card-to-detail inside a tab (Practice to setup, Learn to unit, You to sub-pages), keep the route in the branch. A normal `Hero` then works and the dock stays visible, which is what premium apps do.
  2. **Container transform across navigators.** For full-screen hand-offs (Start a mock to the runner, a result card to the result screen), pass the source rect in `extra` and animate a clip in a `CustomTransitionPage`. That works across navigators and needs no relayout per frame:

```dart
// source
final box = cardKey.currentContext!.findRenderObject()! as RenderBox;
context.push('/result/$id', extra: OriginRect(box.localToGlobal(Offset.zero) & box.size));

// page builder
transitionsBuilder: (ctx, anim, sec, child) {
  final origin = (state.extra as OriginRect?)?.rect;
  if (origin == null || Motion.reduced(ctx)) return FadeTransition(opacity: anim, child: child); // deep link / restore
  final screen = Offset.zero & MediaQuery.sizeOf(ctx);
  final t = CurvedAnimation(parent: anim, curve: Motion.emphasized, reverseCurve: Motion.emphasized.flipped);
  return AnimatedBuilder(animation: t, child: child, builder: (_, child) => ClipRRect(
    clipper: RectRRectClipper(Rect.lerp(origin, screen, t.value)!, lerpDouble(24, 0, t.value)!),
    child: FadeTransition(opacity: CurvedAnimation(parent: anim, curve: const Interval(0.15, 0.6)), child: child),
  ));
}
```

   `extra` does not survive deep links or state restoration, hence the fade fallback.
- **Android 16 predictive back.** The M06 runs Android 16. Apps targeting the newest SDK get predictive back animations by default, so verify against the current Android 16 behaviour changes. Custom `transitionsBuilder`s must look right when the back gesture drives `animation` partway and cancels. Test every custom page on the device with the back gesture, not just the button.
- **Tab switches:** keep `FadingBranchContainer` (branches stay mounted), but give it a 6-8 dp shared-axis shift plus the fade. Keep it at 200 ms or less.

## 5. Spring physics and motion tokens

- **API:** `SpringDescription.withDurationAndBounce({duration = 500 ms, bounce = 0})` is a factory in the current SDK. Designers can then specify "380 ms, bounce 0.18" directly. `withDampingRatio` is still available.
- **Run it on an unbounded controller:** `AnimationController.unbounded(...).animateWith(SpringSimulation(spring, from, to, velocity))`. Springs keep their velocity when interrupted. That is the main reason premium apps feel "physical".
- **Proposed tokens** (they replace the cubic-only `Motion` class; keep `Motion.reduced` and `ReducedMotionScope`):
  - `Springs.snappy` (240 ms, 0): presses and toggles.
  - `Springs.smooth` (380 ms, 0.1): dock lens, cards and sheets.
  - `Springs.bouncy` (520 ms, 0.28): celebrations and Mobi only.
  - `Springs.sheet` (420 ms, 0): drag hand-off with velocity.
- **Delete the "no `BackdropFilter`" rule** in `motion.dart` and the "everything pre-flattened, no saveLayer" rule in `mm_colors.dart`. Replace them with the budgets in section 11.

## 6. Scroll-linked parallax and depth

- **Use paint-only parallax.** Use `Flow` with a `FlowDelegate` that has `repaint: Scrollable.of(context).position` (the Flutter cookbook pattern), or `Transform` driven by a `ValueListenable` of the scroll offset. Never call `setState` per scroll frame, and never relayout.
- **Large-title collapse:** use `CustomScrollView` + `SliverPersistentHeader` with transform and opacity only. A header that blurs live counts against the glass budget (B3).
- **Depth cues that cost nothing:** scale cards 0.98 to 1 as they enter the viewport, use a 2-4 dp parallax on art inside cards, and drift atmosphere blobs at 0.2x the scroll speed.
- **Stop animations you can't see.** Branches that are offstage already use `TickerMode(enabled: false)`. Do the same for any atmosphere that scrolls out of view (`VisibilityDetector`-style checks, or just tie it to the route being current).

## 7. Animation runtimes: Rive vs Lottie vs hand-written

| | Hand-written (Flutter transforms, springs, CustomPainter, shaders) | Lottie (`lottie` package, pure Dart) | Rive (`rive` 0.14.x + `rive_native`) |
|---|---|---|---|
| Runtime cost | Lowest. Same pipeline, fully controllable | Re-paints vector paths every frame through the canvas. Masks and mattes become `saveLayer`s. `frameRate: FrameRate.composition` caps a 30 fps animation so it doesn't paint at 90. `renderCache` trades memory for CPU | `Factory.rive`: its own renderer drawing into a texture, which is efficient for many instances (`RivePanel` shared texture). `Factory.flutter`: paints through Impeller |
| APK size | 0 | Small (Dart only) + JSON assets | **Adds native libraries per ABI.** No published figure, so measure with `--analyze-size`. Wikimedia's evaluation noted a "substantial" size increase |
| Interactivity | Full | Playback and segments only | State machines with inputs: best-in-class |
| **Who can author it here** | **Claude / Codex can write and test it** (goldens, widget tests) | Hand-written JSON for simple loops, or the LottieFiles/After Effects pipeline | **Rive editor only** (a binary `.riv`). Agents cannot author it. Needs a designer and a Rive plan (check current export terms) |
| Low-end risk | Low | Medium (complex AE files) | Low to medium (an extra GPU texture; maturity of `rive_native` on Mali to be checked in B8) |

**Recommendation:**
- **UI motion:** all of it hand-written (dock, cards, numbers, sheets, transitions).
- **Mobi:** rebuild as a **code-driven rig**. Use layered parts (body, visor, eyes, antenna, arms) as SVG compiled with `vector_graphics` or as small WebP layers, plus springs:
  - blink on a jittered timer;
  - the antenna on a spring;
  - eyes that follow the last touch;
  - squash on tap;
  - pose blends.

  That is about 30 KB of assets, agents can author it, and it costs effectively zero at runtime. Use Rive **only if** the owner brings in a Rive designer for a few hero moments (cold open, celebration). Even then keep one Rive instance per screen and benchmark both factories (B8).
- **Lottie:** only for licensed one-off flourishes, with `frameRate` capped.
- **SVG:** prefer `vector_graphics` (precompiled at build time) over `flutter_svg` runtime parsing for illustrations. Icons stay on the Lucide font.

## 8. Animated and mesh gradients, cheaply

Cheapest first:

1. **Pre-rendered gradient art**, WebP decoded at **quarter resolution** (`cacheWidth: 180`) and scaled up with `FilterQuality.low`. Low-frequency art loses nothing. Decoded memory: 180x400x4 = 288 KB, against 4.6 MB at full resolution.
2. **Drifting blobs.** Two or three pre-blurred radial blobs (images, or `RadialGradient` circles) moved and scaled slowly with transforms, inside a `RepaintBoundary`. GPU cost is a few textured quads. **This is the recommended "living" background**, and fake glass (2.2) can draw the same blobs blurred.
3. **Full-screen fragment-shader mesh** (`mesh` package 0.5.0, MPL-2.0, or our own 4-point gradient shader). That is about 1.15 Mpx of per-pixel maths **every frame at 90 Hz** on a 2-core Mali. It also forces every live blur above it to re-run each frame. Use it only on the Welcome/cold-open, only if B7 shows a raster p90 at or below 6 ms, and pause it after 6-8 s or once the user starts acting.

`mesh_gradient` (widget-based) is another option. Treat both packages as references; our own 30-line shader is easier to tune and audit.

## 9. Raster art from image generation (ChatGPT / Codex images)

**Resolution:**
- The M06 uses `2.0x` assets (DPR about 1.875, about 384 dp wide).
- **Full-bleed art:** 768x1706 px (2.0x) is enough. Flagships (DPR 2.75-3.5) upscale it slightly, which is fine for soft atmospheric art. For crisp objects, add `3.0x` variants.
- **Objects and stickers** at 160 dp: export 320 px (2.0x) and 480 px (3.0x).
- Generators output about 1024-1536 px, which covers all of the above. Never bake **text** into generated images; text stays live for accessibility and copy changes.

**Format and sizes:**
- Lossy WebP: `cwebp -q 80 -m 6`. For cut-outs add `-alpha_q 90`.
- Expected sizes: atmosphere at 768x1706 about 60-140 KB; a 480 px sticker with alpha about 25-60 KB; a mascot layer about 5-15 KB.
- Avoid AVIF: Flutter's built-in codecs don't decode it.
- Animated WebP works, but it decodes on the CPU per frame. Use it only for tiny loops.

**Memory:**
- Decoded size is width x height x 4.
- Always pass `cacheWidth` equal to the rendered pixel width, or less for soft art.
- Cap the cache: `PaintingBinding.instance.imageCache.maximumSizeBytes = 48 << 20`.
- `precacheImage` the Welcome and onboarding art during splash.

**Consistency:** write a one-page "image bible" before generating anything: palette, lighting direction, material (glossy 3D vs flat), grain, and the framing rule. Generate in batches against it. Mixed styles read as cheaper than no art.

**Video:** not needed for the app.
- A short H.264 loop through `video_player` (ExoPlayer texture) is feasible for a cold-open (720p, 3-6 s, 1-2 MB) and the hardware decoder handles it, but it is another texture layer and has a start-up delay.
- Drifting blobs, the Mobi rig and pre-rendered art cover the same feeling at a fraction of the cost.
- Video generation would be more valuable for the website hero and the Play Store promo than inside the app.

## 10. Type: variable fonts and a premium feel

- **Current fonts:** Gabarito (display) and Hanken Grotesk (text) ship as 9 static TTFs (812 KB). Both exist on Google Fonts as **variable** fonts (wght axis). Swapping to the two variable files lowers the size and lets us use any weight (for example 650 for numbers).
- **Weight behaviour:** since Flutter 3.41, `FontWeight` also drives the `wght` axis automatically.
- **Animating weight:** keep the same axis list and order in both styles. The fast path interpolates `fontVariations`. Each distinct weight value adds new glyphs to Impeller's glyph atlas, so **animating weight continuously on big text can churn the atlas**. Allow it only on short labels or a single hero word (B11), never on body text.
- **Tabular figures:** `fonts.dart` notes Gabarito has `tnum` and Hanken does not. Any replacement face must be checked for `tnum` before we adopt it, because marks, timers and counts must align.
- **If the brand moves to a new face:** OFL options with genuine personality for a Gen-Z audience include Bricolage Grotesque (opsz, wdth and wght axes), Unbounded, Instrument Sans and Geist. Fontshare faces (for example Clash or Satoshi) are free under the ITF licence; read the app-embedding clause before using one.
- **Licensing:**
  - **Google Fonts (OFL):** embedding in a commercial app is allowed. Bundle the files: don't fetch them at runtime with `google_fonts`, which needs a network connection and causes a flash.
  - **Licence text:** register it through `LicenseRegistry.addLicense`; the OFL text files are already in `assets/fonts`.
  - **Subsetting:** under the OFL a subset counts as a modified version. Don't subset fonts that have a Reserved Font Name; just ship them whole.

## 11. Haptics on Samsung One UI

- **Built-in calls:** Flutter's `HapticFeedback` now has `selectionClick`, `lightImpact`, `mediumImpact`, `heavyImpact`, `vibrate`, plus **`successNotification`, `warningNotification` and `errorNotification`**. On Android these map to `performHapticFeedback` constants: selection to a clock tick, light to a virtual key, medium to a keyboard tap.
- **What that means on Samsung:** One UI scales these through its system vibration intensity and **"System vibration" toggle**, so they can be faint, or silent when the toggle is off. That is correct behaviour: it respects the user.
- **The M06 motor:** budget phones usually have a coarse motor. Crisp "tick" haptics may feel like buzzes. Test the vocabulary on the device (B12) and drop any verb that feels mushy.
- **Map the existing `Haptics` verbs onto the new calls:**
  - `success()` uses `successNotification`, for things the server has acknowledged: submission, repair finished, goal met.
  - `warn()` uses `warningNotification` instead of the two-light-impacts hack.
  - Errors and wrong answers still get no haptic (keep that rule).
- **Amplitude control:** only through a small platform channel to `Vibrator`. Check `hasAmplitudeControl()` and `areAllPrimitivesSupported(PRIMITIVE_CLICK)`, then use `VibrationEffect.createOneShot(ms, amp)` or `startComposition().addPrimitive(...)`. This path **ignores the system touch-feedback toggle**, so gate it behind our own Touch feedback switch, and use it only for one or two signature moments (a celebration). Budget phones often lack primitives, so keep a fallback.

---

## 12. Performance budget (targets until measured on the M06)

| Metric | Budget |
|---|---|
| Refresh | Design for 90 Hz (11.1 ms). If key flows cannot hold it after optimisation, request 60 Hz on the M06 through a display-mode plugin: a steady 60 beats a stuttering 90 |
| UI thread (build + layout) | p90 ≤ 6 ms, p99 ≤ 10 ms on Today, Practice, Review, the dock and the runner |
| Raster thread | p90 ≤ 8 ms, p99 ≤ 11 ms at 90 Hz. The runner and repair must stay ≤ 6 ms p90 (no glass there) |
| Missed frames | ≤ 2% in a scripted scroll + tab-switch run; ≤ 5% during page transitions |
| Live backdrop blurs | ≤ 2 visible at once (dock + one sheet or header), all under one `BackdropGroup`, ≤ 25% of the screen area in total |
| Full-screen animated layers | ≤ 1 per screen. Paused when offscreen, after 8 s idle and under reduced motion |
| Runtime shaders | ≤ 1 live per screen, precached at splash |
| Memory (PSS) | ≤ 220 MB steady, ≤ 280 MB peak (`dumpsys meminfo`); image cache 48 MB; watch the "GL mtrack / Graphics" row for blur textures |
| Raster assets in APK | ≤ 3 MB at first release; full-bleed WebP ≤ 150 KB each |
| APK (arm64 split) | Measure the current size first. Growth from the redesign ≤ +5 MB, Rive included |
| Cold start | ≤ 1.5 s to first frame, ≤ 2 s to an interactive Welcome (profile build) |
| Thermal | 10 minutes of mixed use with no throttling-induced rise in jank above 5% |

**How to measure** (profile builds only; debug timings mean nothing):

- **Launch and watch:** `flutter run --profile -d R9ZY9056DVF`, then DevTools > Performance (frame chart, raster vs UI, "Track widget builds"). The Performance overlay is good for a quick look.
- **Scripted benchmarks:** `flutter drive --profile --driver=test_driver/perf_driver.dart --target=integration_test/<bench>_test.dart`. Use `binding.traceAction` and `TimelineSummary`, which writes average, p90 and p99 build and raster times plus missed-frame counts to JSON. Commit the JSONs under `docs/brain/design-2026-10-13/bench/`.
- **In-app sampling:** `SchedulerBinding.addTimingsCallback` feeds a debug HUD and the adaptive-quality logic.
- **Refresh rate:** `adb shell dumpsys display | grep -iE "refresh|fps"` and `adb shell settings get system peak_refresh_rate`.
- **Which renderer:** `adb logcat -s flutter`, looking for the Impeller backend line.
- **Memory:** `adb shell dumpsys meminfo in.mockmob.app`.
- **`adb shell dumpsys gfxinfo in.mockmob.app framestats` is of limited use.** Flutter draws into its own surface, outside Android's HWUI pipeline, so treat gfxinfo as a sanity check only. Use the Flutter timeline, or Perfetto (`adb shell perfetto`, with GPU frequency and thermal tracks) for presentation timing.
- **Size:** `flutter build apk --release --split-per-abi --target-platform android-arm64 --analyze-size`.
- **Test conditions:** run each benchmark warm, three times, with the battery above 50% and power saving off. Also run once with power saving **on**, because many students will have it on. Owner's device rule: test on the phone, not an emulator.

## 13. Micro-benchmarks to run on the M06 before committing

Build these as a hidden `/lab` route compiled only in profile builds, plus one integration test each.

| # | Benchmark | Decides |
|---|---|---|
| B1 | Read the refresh rate, density and Impeller backend; cold start of the current app | Baseline: 90 or 60 Hz design, Vulkan confirmed |
| B2 | Glass dock (real blur, sigma 12 / 20 / 30) over a fast-flung list of image cards, 60 s | Whether the dock can be real glass, and at which sigma |
| B3 | Dock + blurred sticky header (+ an open sheet), **grouped vs ungrouped** | Whether a glass header is allowed; how much `BackdropGroup` saves |
| B4 | Ten cards: fake glass (2.2) vs `BackdropFilter` per card, over drifting blobs | Confirms the main technique; size of the gap |
| B5 | `liquid_glass_renderer` dock (`LiquidGlass` vs `fake: true`): 2 min of tab switching, PSS over time | Whether we vendor the package's shader or skip it |
| B6 | Our lens shader on the dock indicator only (`ImageFilter.shader`), plus first-use hitch with and without precache | Refraction lens yes or no |
| B7 | Atmosphere: shader mesh at full resolution vs drifting pre-blurred blobs vs static WebP; 5 min warm, under a live dock | Background technique per screen |
| B8 | Mobi: code rig vs Rive (`Factory.rive` and `Factory.flutter`) vs Lottie: idle + state change; frame times, PSS, APK delta | Mascot runtime |
| B9 | Container transform Practice card to the root-navigator result route, with the dock visible; predictive-back gesture scrub | Transition approach and back-gesture correctness |
| B10 | Parallax list with 20 image cards (`cacheWidth` set), 3 min fling loop | Parallax and image-memory budget |
| B11 | Animated weight on one 40 sp word vs a cross-fade of two static weights | Whether variable-weight animation is allowed |
| B12 | Haptics feel on the device: every `HapticFeedback` verb, `hasAmplitudeControl`, primitives support | Final haptic vocabulary |
| B13 | Full flow with new art: cold start, Welcome to onboarding to Today, PSS peak, APK size | Asset and memory budgets hold |

**Pass rule:** a technique ships on the M06 at "Full" only if its benchmark meets section 12 at the device's real refresh rate. Otherwise it ships as "Lite" on low-tier devices and "Full" elsewhere.

---

## 14. Current code: what to replace and what to keep

**Keep as is.** These are the product's spine and contain no design decisions:
- `lib/core/api`, `auth`, `repositories`, `storage` (drift), `sync` including **`sync/session` (the session engine, journal, heartbeat, clock)**.
- `domain`, `analytics`, `connectivity`, `permissions`, `notifications` logic, `settings`.
- The feature data and state layers (`features/*/data`, `logic`, `state`, `model`).
- `copy/formatters.dart`.

**Keep, with changes:**

| File(s) | Change |
|---|---|
| `core/router/router.dart`, `routes.dart`, `router_redirect.dart`, `action_router.dart` | Routes, redirects and deep links stay. Re-home routes that should share-element into their branch (section 4), and add `extra: OriginRect` to full-screen hand-offs. The onboarding routes (`/onboarding/subject`, `/onboarding/sample/:i`, `.../result`) will change with the new onboarding flow |
| `core/router/app_shell.dart` | Becomes `BackdropGroup` + `Stack` with a floating `GlassDock` and `DockInsets` (instead of `bottomNavigationBar`). Keep the re-tap, back-to-Today and review-dot logic |
| `core/router/transitions.dart` | Keep `mmPage` and `FadingBranchContainer` structure; new curves and springs, a shared-axis tab switch, a container transform, predictive-back-safe builders |
| `core/motion/motion.dart`, `reduced_motion.dart` | Keep `Motion.reduced` and the scope. Add `Springs` and choreography tokens; delete the "no BackdropFilter" rule. Add `GlassQuality` beside reduced motion |
| `core/haptics/haptics.dart` | Keep the provider, the switch and the test driver; add `success` and `warn` on the new API, plus an optional amplitude channel |
| `core/widgets/mobi.dart` | Keep the API (pose, size, semantics); the implementation becomes the code rig |

**Replace** (the design system):

| File(s) | Why |
|---|---|
| `core/theme/*` (`mm_colors.dart`, `mm_type.dart`, `tokens.dart`, `theme.dart`, `fonts.dart`) | The colour model is "every wash pre-flattened, nothing translucent", which glass cannot use. The new tokens need translucency roles (tint by role and theme), light and edge tokens, atmosphere palettes, elevation, and type roles for the brand face (variable files) |
| `core/widgets/bottom_nav.dart` | Becomes `GlassDock` (section 3) |
| `core/widgets/key_button*.dart` | The 3D keycap with a lip is the most visible "old identity" element. Rebuild the primary action against the new language; keep the commit-on-release, loading and disabled-reason behaviour and its tests |
| `core/widgets/mm_sheet.dart` | Becomes a glass sheet with spring drag and velocity hand-off |
| `inline_banner`, `state_view`, `skeleton`, `week_strip`, `question_strip`, `save_pill`, `receipt_line`, `mm_spinner` | Restyle on new tokens. The behaviour and semantics in them stay (`save_pill` and `receipt_line` encode the "never show success before the server acknowledges" rule) |
| `core/router/splash_screen.dart` | Branded cold-open, which also precaches the shaders and art |
| All feature **screens and widgets** (`features/*/screens`, `widgets`), onboarding entirely | Rebuilt on the new system. Their providers stay |
| Copy: `features/onboarding/copy.dart` (`notAffiliated`, `sampleDisclaimer`), `features/you/copy.dart` (`helpNonAffiliation`), and the "This is practice, not proof." tails in `core/copy/state_words.dart` and `features/practice/copy.dart` | Per the owner, remove the defensive footers and taglines. The **integrity rule stays in behaviour, not in disclaimers**: practice results are labelled and stored as practice and are never shown as improvement. Non-affiliation can live once in Help > About |

**Tests:** goldens for the widgets above will all be regenerated. The logic tests (auth 68, onboarding 96 per the last handover) for data and state should survive untouched. That is a useful check that the redesign did not touch the spine.

## 15. Recommended sequence

1. **Before any design is final:** run B1 and B2 (half a day). They decide 90 vs 60 Hz and whether the dock is real glass.
2. Build `core/glass` (`GlassSurface`, `AtmosphereCache`, `RenderFakeGlass`, `EdgeLightPainter`, `GlassQuality`) and the `/lab` route. Run B3-B7.
3. New tokens and theme, the dock, the shell and transitions (B9). Then the Mobi rig (B8).
4. Screens, in the order the owner sees them: cold-open, onboarding, Today, Practice, Review, Learn, You.
5. B13 and the adaptive-quality default for the M06; then the owner's phone pass.

## Sources

- Flutter "What's new" posts for [3.19](https://flutter.dev/blog/whats-new-in-flutter-3-19) (backdrop speedups), [3.22](https://flutter.dev/blog/whats-new-in-flutter-3-22) (blur rewrite), [3.29](https://flutter.dev/blog/whats-new-in-flutter-3-29) (`BackdropGroup`) and [3.44](https://flutter.dev/blog/whats-new-in-flutter-3-44) (Vulkan memory and sync, uniforms by name, HCPP).
- Flutter API reference: [BackdropGroup](https://api.flutter.dev/flutter/widgets/BackdropGroup-class.html), [BackdropFilter.grouped](https://api.flutter.dev/flutter/widgets/BackdropFilter/BackdropFilter.grouped.html), [ImageFilter.shader](https://api.flutter.dev/flutter/dart-ui/ImageFilter/ImageFilter.shader.html), [SpringDescription](https://api.flutter.dev/flutter/physics/SpringDescription-class.html), [HapticFeedback](https://api.flutter.dev/flutter/services/HapticFeedback-class.html).
- Impeller engine source and docs: [driver_info_vk.cc](https://api.flutter.dev/impeller/driver__info__vk_8cc_source.html) (bad-driver list; Mali absent), [Impeller docs](https://docs.flutter.dev/perf/impeller), [the Impeller Android doc](https://flutter.googlesource.com/mirrors/engine/+/refs/heads/main/impeller/docs/android.md), [engine PR #55701](https://dart.googlesource.com/external/github.com/flutter/engine/+/ad9e4fef451a73427285826455db5fbdde502bd7%5E%21/) (sharing backdrop inputs).
- Breaking change: [FontWeight drives the wght axis](https://docs.flutter.dev/release/breaking-changes/font-weight-variation) (3.41).
- [liquid_glass_renderer on pub.dev](https://pub.dev/packages/liquid_glass_renderer) and its README via Context7 (`/whynotmake-it/flutter_liquid_glass`).
- [rive on pub.dev](https://pub.dev/packages/rive) and the rive-flutter docs via Context7 (`/rive-app/rive-flutter`): renderer factories and `RivePanel`.
- [Wikimedia T433250](https://phabricator.wikimedia.org/T433250) (Rive size note) and the [Callstack Lottie vs Rive comparison](https://callstack.com/blog/lottie-vs-rive-optimizing-mobile-app-animation).
- [mesh on pub.dev](https://pub.dev/packages/mesh) and [mesh_gradient docs](https://pub.dev/documentation/mesh_gradient/latest/).
- M06 specs: [91mobiles](https://www.91mobiles.com/samsung-galaxy-m06-price-in-india) and [Smartprix](https://www.smartprix.com/mobiles/samsung-galaxy-m06-ppd1e0j4ujzx).
- Repo precedent: `C:\Users\atish\Desktop\CampusOS\lib\core\widgets\glass.dart` (the GlassQuality full/lite and edge-light pattern, built for the owner's HIGH-inspired design system).
