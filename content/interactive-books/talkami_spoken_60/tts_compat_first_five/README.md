# New spoken 60: first five themes for old Talkami batch TTS

Original new JSONs have `scenes[].phrases[]` and canonical IDs containing dots (example `01.01.01-S001`). Older batch dubbing tools accepted `lessons[].phrases[]` and IDs like `s01_01_0001` and could not parse the new source directly.

These 5 standalone JSONs use the *old import structure* and temporary old-style IDs. **They are NOT replacements for canonical course files.** After dubbing, you MUST translate MP3 names back to canonical IDs with the corresponding mapping.

| Theme | Canonical source | Main sentences | Reply/alternatives | MP3 count |
|---|---|---:|---:|---:|
| 01 | 01.01 | 103 | 110 | 213 |
| 02 | 01.02 | 63 | 69 | 132 |
| 03 | 01.03 | 75 | 72 | 147 |
| 04 | 01.04 | 93 | 114 | 207 |
| 05 | 01.05 | 96 | 97 | 193 |
| **Total** | | **430** | **462** | **892** |

## Workflow

1. Import `01_tts_compat.json`, `02_tts_compat.json`, etc **one theme at a time** into your older TTS HTML. New source Chinese/Burmese/pinyin/phonetics are preserved. Do not rename canonical course IDs.
2. After MP3 generation and ZIP export, for each theme run `python remap_tts_zip.py "tts-export.zip" "01_id_mapping.json" "01.zip"` (replace 01 with the corresponding theme number). This script produces an app-compatible ZIP containing `audio/01.01.01-S001.mp3` and its reply/alt variants.
3. Verify the ZIP contains exactly the expected number of MP3s, or the current Mini App will not accept it. Every MP3 <=512 KB, each ZIP <=30 MB, <=300 clips. The resulting ZIP SHA-256 must be pinned to the app manifest.
4. The Mini App's first five lessons can be distributed with the app as static assets rather than R2, but this requires a separate application change after all recordings exist. These files alone do not ship audio.

This adapter uses stable aliases such as `s01_11_0001` => `01.01.01-S001` to avoid colliding with previous recordings. Never map by ordinal position because source sentences have been re-ordered.

Content source updated 2026-11-11; status: `draft_pending_native_review` (Burmese/pronunciation editorial review pending).
