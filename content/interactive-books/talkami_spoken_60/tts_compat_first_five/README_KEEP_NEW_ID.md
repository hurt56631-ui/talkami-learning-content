# Android TTS compatibility — unchanged canonical IDs

For older Android Talkami dubbing App JSON loaders which require `lessons[].phrases[]`, the five files `01_tts_old_format_keep_new_id.json` through `05_tts_old_format_keep_new_id.json` restore the original V13 JSON structure (including `theme_id`, `theme_title`, `lesson_id`, `level`, `replies`, `alternatives`, `pinyin`, and `phonetic_my`).

**Preferred workflow:** Import each `NN_tts_old_format_keep_new_id.json` in the Android dubbing app. The phrases **keep their canonical IDs**, such as `01.01.01-S001`. The resulting MP3 may then retain these names and can be bundled in the Mini App directly with **no ID remapping**.

If the Android app rejects dots or hyphens in IDs (not just the JSON nesting), use the alternative files `NN_tts_compat.json` with old-style generated IDs and then convert exported MP3 names back to canonical IDs using `NN_id_mapping.json` and `remap_tts_zip.py`.

The canonical website course JSON under `packs/new_spoken_60/` was not changed.

- Theme 01, source 01.01: 103 main, 110 reply/alt MP3, 4 lessons, e.g. `01.01.01-S001`
- Theme 02, source 01.02: 63 main, 69 reply/alt MP3, 3 lessons, e.g. `01.02.01-S001`
- Theme 03, source 01.03: 75 main, 72 reply/alt MP3, 3 lessons, e.g. `01.03.01-S001`
- Theme 04, source 01.04: 93 main, 114 reply/alt MP3, 4 lessons, e.g. `01.04.01-S001`
- Theme 05, source 01.05: 96 main, 97 reply/alt MP3, 3 lessons, e.g. `01.05.01-S001`

These files preserve the draft Chinese/Burmese content, pending final Myanmar-native and pronunciation review.
