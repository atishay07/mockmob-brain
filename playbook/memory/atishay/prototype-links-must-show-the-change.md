---
name: prototype-links-must-show-the-change
description: "3 Nov: the owner opened the LAN prototype and saw \"exactly the same as before\", no Learn tab and \"Chapter feeds did not load\" — the preview harness hides Learn v2 unless decks=real&study=on; open every link at phone size first"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c4dbd3b5-f204-4be3-b317-5f8ec24375d4
  modified: 2026-11-03T09:28:20.202Z
---

On 3 Nov 2026 (~3:15 pm IST) the owner judged the r6 LAN prototype (top bar + Web D cards) on his phone: "It looks exactly the
same as before ... There is no way to access the learn section ... it's showing 'Chapter feeds did not load.' ... card look is
the exact same as before." The plain `/preview/arena?view=dashboard` view runs without Learn v2 (no Learn tab, Explore covers
fail), so the new cards were never on his screen.

**Why:** he judges only what the live link shows; a link that does not land on the changed screen reads as "nothing changed".

**How to apply:** for every prototype link, open it yourself at 375x812 first and look at the changed part; Learn v2 previews
need `decks=real&study=on` (e.g. `/preview/arena?decks=real&study=on&plan=pro&student=commerce&view=learn2-feed&chapter=...`).
Give him one link per change that lands directly on it, with one line saying what to look at. Use the PC's Wi-Fi
address 192.168.1.8 (192.168.1.15 is Ethernet and the firewall's node rule only allows the Private Wi-Fi profile; never
change firewall settings). A phone demo APK's DEMO_LEARN_BASE must use .8 too. Related:
[[live-prototype-over-renders]].
