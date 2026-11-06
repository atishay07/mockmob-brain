---
name: mockmob-upload-key
description: 19 Oct: MockMob's Play upload keystore, key.properties and PLAY_RTDN_TOKEN live in C:\Users\atish\MockMob-keys (outside git); copy key.properties into a build worktree to sign
metadata:
  type: reference
---

Created 19 Oct 2026 at the owner's request (D123) with `flutter_app/tool/make_upload_key.ps1`:
- `C:\Users\atish\MockMob-keys\mockmob-upload.jks` (alias `upload`, PKCS12), `key.properties` (points at the jks; copy it to `<worktree>/flutter_app/android/key.properties` before `tool/build_release_aab.sh`), `READ-ME-BACK-ME-UP.txt` (password), `PLAY_RTDN_TOKEN.txt`.
- Upload key SHA-1 BA:E6:93:5D:...:27:D5; SHA-256 62:AC:58:08:...:EC:47 (full values in the keystore; `keytool -list -v`).
- Builds before 19 Oct were debug-signed: installing an upload-key-signed or Play-signed build over them needs an uninstall first.
Never print the password in chat or commit any of these files. Related: [[security-fixes-deploy-immediately]].
