# Talkami 缅甸学生中文句型 · 三卡教材 V3

截至 2026-11-19：基于原有 500 个句型编写 **16 类、500 个完整三页句型卡**。

## 已完成的内容

- 500 个句型，原 `id`、`number`、`title`、`formula`、`example`、`introduction` 均保留
- 500 × 3 = **1500 个教学页面（卡片页）**
- 每个句型有 3 个不同中文例句及对应缅语译文，共 **1500 条**
- 每个句型有 2 个模板（基础表达 + 另一场景），共 **1000 个模板**
- 每个句型有 1 组包含 2 轮的 A/B 情境对话，共 **500 组**
- 对确定有教学价值且能判断真假的问题，提供部分常见错误示例，不强制每条编造错误
- 每条都有针对缅甸学习者的 `myanmar.usage_my` 和 `myanmar.example_my`
- 提供 AI 教师 V2 提示词，不强制练习题、跟读或等待学生作答

## 原 Android 页面与三张卡的关系

Android 源码：`wklearning/src/main/java/com/chat/learning/PatternCardActivity.java`
- 第 1 张：`overview` — 结构说明、3 条中缅例句、可朗读
- 第 2 张：`focus` — 2 个模板，每模板 1–2 条中缅例句
- 第 3 张：`usage` — 1 组真实情境的两轮 A/B 对话，可附确实成立的易错提醒

解析器：`PatternCardData.java`，读取 `card.pages`（不是读取 `myanmar` 自动生成页面）。

**注意：** 文字卡是 Android 原生三页布局，无需重新设计 UI。左右滑换页、上下滑换句型、页面底部可打开 AI 追问。

## 文件结构

```text
content/patterns/
├── catalog.json                    # V3 分类目录：源数据/版本/发布文件名
├── packs/
│   ├── pattern_cat_01_v1.json       # 原版存档，仍保留
│   ├── pattern_cat_01_v3.json       # 正式候选来源，45 条完整三卡
│   ├── ...                         # 02~15 同理
│   └── pattern_cat_16_v3.json       # 5 条完整三卡
└── prompts/
    ├── pattern_analysis_v1.txt     # 原 AI 提示词，仍保留
    └── pattern_analysis_v2.txt     # 缅甸视角新提示词

exports/myanmar_patterns_v1/
├── catalog.json                    # 独立版目录
├── all_patterns_mm.json            # 500 条合并版 JSON（体积较大，建议使用 Raw）
├── packs/
│   └── pattern_cat_XX_mm.json      # 16 份独立编辑/分享副本
├── editorial/
│   └── pattern_cat_01_extra.json   # 第一类例句的初期编辑参考
├── ai_teacher_prompt.md            # 提示词编写说明
└── README.md

scripts/check_pattern_v3.py         # 严格校验 500 条与三卡字段
.github/workflows/check-pattern-v3.yml
```

## 怎么修改某个句型

1. 找到编号。例如 347 号“把字句”在 `content/patterns/packs/pattern_cat_10_v3.json`。
2. 找到 `"id": "pattern_347"`。
3. `myanmar.example_my` 是原中文首例句的缅文；`myanmar.usage_my` 是解释。
4. `card.pages[0].items` 是卡一的三条例句。
5. `card.pages[1].templates` 是卡二的模板及例句。
6. `card.pages[2].dialogues` 和 `mistakes` 是卡三的情境问答和易错说明。
7. 修改后运行 `python scripts/check_pattern_v3.py`，再运行 `python scripts/build_release.py`。
8. 审校通过以后，合并 Draft PR 并按既有 `Publish learning content` 流程发布新 GitHub Release。

## 发版注意

- 新版不覆盖 `_v1.json`。发布目标文件名为 `pattern-*-v3.json`。
- `content/patterns/catalog.json` 已在 PR 分支内指向 V3，包含 `source_data`；打包脚本负责写入 SHA-256/大小/版本，**不要把仓库源目录直接作为 Android 下载目录**。
- 数据尚未发布到当前 Android 所读取的最新 Release，线上用户不会自动获得更新。
- 部分缅语是教学编辑初稿，**未经过独立缅语母语教师逐条终审**；为避免错误扩散，此 PR 保持草稿，不自动合并、也不触发正式发布。
- 本批未额外生成拼音与音频文件；Android 中文句子可按原有 TTS 桥接播放。

## 质量校验

在 PR 分支已完成基于真实 JSON 的结构检查：16 类，500 个不重复 ID，连续编号 001–500，1500 条中缅例句，1000 个模板，500 组两轮对话，三页类型及 JSON 必填字段均齐全。还人工校正了部分中文搭配、数字表达、缅语方向性翻译及容易错误定性的示例。

结构检查不代表母语终审；上架前应抽检全部 500 条，优先复核细微语气、多音字/时间数量、多义词、语用差异。
