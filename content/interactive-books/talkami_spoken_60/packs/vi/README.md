# Talkami 越南语短句（独立数据目录）

这里是越南语独立版本：`content/interactive-books/talkami_spoken_60/packs/vi/`，不覆盖原缅语版本 `packs/01.json`–`packs/60.json`。

## 当前进度（2026-11-02）

- 已发布主题：**01–35**，共 **2567 张主卡**。
- 越南语课程目录：`catalog.json`，已登记 35 个主题，供越南语 App 加载。
- 主题数据文件：`01.json`–`35.json`。
- 第36–60主题尚未制作成正式越南语课程文件。
- 部分辅助文件包括 `_translation_map_*.json`、`_translation_notes_*.json` 和 QA 报告，仅供制作及审核使用；辅助文件的存在不代表正式课程已经发布。

## 数据原则

- 保持中文 `text`、拼音 `pinyin`、ID、课程顺序、等级以及 `alternatives`、`replies` 的原结构。
- 中文对应的越南语译文使用 `meaning_vi`；教学提示使用 `text_vi`；课节与主题采用 `title_vi`、`theme_title_vi` 等字段。
- 去除缅语的 `_my` 翻译和 `phonetic_my`（它是缅文字母模拟的汉语读音，不适用于越南学习者）。
- 原课程中带有缅甸国籍、文化或情境的中文例句，原则上保留原中文，必要时在越南语教学提示中解释，不随意更改稳定中文语料。
- 越南语 App 应读取 `_vi` 字段，并使用本目录专有的 `catalog.json`，不可直接沿用原缅语目录。

## App 数据入口

- [越南语目录](https://raw.githubusercontent.com/hurt56631-ui/talkami-learning-content/main/content/interactive-books/talkami_spoken_60/packs/vi/catalog.json)
- 单个主题按 `packs/vi/<theme_id>.json` 加载。例如第35主题的路径是 `packs/vi/35.json`。

## 第31–35主题新增翻译（2026-11-02）

本批完成5个主题，共**378张主卡、944条替换句/回应句、318条越南语教学说明**；与原始中文逐卡核验，修复退款回应顺序并复查金额/物流/方位等高风险语义。详见 [`QA_31-35_NATURALNESS_20261102.md`](QA_31-35_NATURALNESS_20261102.md)。原始缅甸语包未改动。

## 质量声明

已完成第01–30主题翻译自然度与语义专项复查：核对 **2189张主卡、5931条替换/回应句、2095条教学提示** 的数据完整性及重点语义，本轮在19个课程文件内修正54处表达/教学字段，并同步升级对应课程版本。复查详情见 [`QA_01-30_NATURALNESS_20261102.md`](QA_01-30_NATURALNESS_20261102.md)。

**注意：本轮人工语言复核以所有主卡和高风险附属表达为重点，不代表5931条附属句都已获得独立越南语母语审校。** 原音频与 App 真机加载测试仍需完成，正式商用前建议由越南语母语编辑终审。
