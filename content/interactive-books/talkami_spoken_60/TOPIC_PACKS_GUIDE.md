# Talkami 综合口语书｜在线数据的唯一来源（2026-10-12）

当前网页阅读器从 `catalog.json` 读取主题列表，再按 `data_url` 获取 `packs/<主题编号>.json`，按 `data_version`区分更新缓存；旧版主题包在main同一文件路径被新版直接替换，不保留可并行加载的旧包。

`source/<主题编号>.json` 是本主题可编辑教学源稿（含`source_links`），不是另一套在线旧卡；网页只加载`packs/`。`source_links`是跨课复用引用，不重复计算为主卡。

2026-10-12已将六个新版发布到main：18家务做饭（93张V4）、21食物口味（90张V4）、22早餐小吃（63张V4）、24餐厅用餐（58张V4）、25餐厅结账（62张V4）、26咖啡奶茶（64张V3），共430张原位替换，无任何重复加卡；23餐厅点餐V2已先前发布。目录共38个已上架主题，2749张主卡（总数不增加），版本39，收费属性、原卡ID和顺序保持不变。

已废弃并移除旧口语阅读器的`book_latest.zip`、`web_catalog.json`及`free/*.json.gz.b64`历史入口（详见LEGACY_CLEANUP_2026_10_11.md）。仍在用户设备上的旧缓存、Android旧版本或外部镜像无法仅靠修改GitHub历史自动删除，需重新加载目录并检查客户端数据来源。

独立的`content/ai_course/分类场景_fenlei_changjing/`保留：它是其他AI教学功能用的`scenes`源素材，不是网页短句阅读器读取的数据；直接删除可能破坏另一功能。

主题34–44（11主题）仍然是尚未逐卡教学精修的已上架旧质量内容；因没有完整新版可替代，不直接删除整课。拼音及缅文近似谐音需要人工审定，这六个主题的新版亦尚未经过独立缅语教师与真人录音终审。


## 2026-10-12 update after themes 40–44

Current catalog is V50: 39 themes are available and 21 are missing. Themes 34–44 are no longer all unrefined: 34–39 and 40–44 have now received per-card bilingual usage and mistake reviews. Themes 40 (56 cards, V3), 41 (58, V5), 42 (57, V4), 43 (50, V4), 44 (66, V4) now have editable source JSONs and updated website packs, 287 published cards in total. Old guide statements about 38 themes and 34–44 remaining unrefined are historical only. Native speaker pronunciation and real-device audio testing are still pending.
