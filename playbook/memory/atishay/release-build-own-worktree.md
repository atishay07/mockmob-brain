---
name: release-build-own-worktree
description: 4 Nov 2026 - the signed AAB build failed because an emulator-walk demo build ran in the same worktree; build releases in a clean detached worktree at the release commit
metadata:
  type: feedback
---

On 4 Nov 2026 (about 7:10 pm) `tool/build_release_aab.sh --sell` in wt-1103-app-rel failed with "package dev.flutter.plugins.integration_test does not exist" in GeneratedPluginRegistrant.java: a re-walk agent's demo debug build (which includes the integration_test dev plugin) was running in the same worktree and rewrote the generated registrant mid-compile. The flutter build lock does not cover the whole sequence.

**Why:** release and demo builds share build/ and android/app/src/main/java in one worktree; concurrent builds corrupt each other.

**How to apply:** build every Play release in its own clean worktree (`git worktree add --detach ../wt-<x>-app-build <release sha>`), `flutter pub get`, copy key.properties (MockMob-keys) and dart_defines/prod.json in, build the AAB and the arm64 APK, verify the signer (Android Studio jbr keytool -printcert for the AAB, build-tools apksigner for the APK; expect SHA-256 62:AC:58:08...EC:47), copy outputs to Desktop/MockMob-build-N, delete the two secret files, then remove the worktree. Windows may refuse `git worktree remove --force` with "Filename too long": delete with PowerShell `Remove-Item -LiteralPath "\?\<path>" -Recurse -Force`, then `git worktree prune`. Related: [[mockmob-upload-key]], [[agent-swarm-resource-hygiene]].
