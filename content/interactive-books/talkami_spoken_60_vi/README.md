# Talkami 中文口语 · 越南语独立版本（制作中）

源数据：`content/interactive-books/talkami_spoken_60/packs/`（main分支，60主题）。

## 已完成
- `translations/01_phrase_map.json`：第01主题全部73张卡片所包含的244条**不重复中文主句、替换说法与回应**的越南语译文。键为原中文原文。
- 该文件是翻译对照表，**不是可直接替换App主题包的最终JSON**。

## 待完成
- 第01主题的课程标题、说明、易错教学点与完整卡片结构中的所有缅语字段翻译。
- 将对应译文填入与缅语App相兼容的完整独立主题包 `packs/01.json`，保留ID、中文、拼音、分级与原句顺序。
- 第02–60主题及越南语 `catalog.json`；逐包校验后再供App接入。

## 隔离原则
- 不覆盖 `content/interactive-books/talkami_spoken_60/` 现有的缅语资源。
- 仅在 `content/interactive-books/talkami_spoken_60_vi/` 保存越南语内容。
- 所有翻译均需越南语母语者进行最终审校，现有翻译不是母语终审结论。
