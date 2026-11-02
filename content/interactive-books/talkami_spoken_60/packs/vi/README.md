# Talkami 越南语短句（独立数据目录）

这里是缅语口语课程的**越南语独立版本**。文件放在 `content/interactive-books/talkami_spoken_60/packs/vi/`。原有 `packs/01.json` 至 `packs/60.json` 仍为缅甸语版本，**不会被覆盖**。

## 当前发布范围（2026-11-02）

- `catalog.json`：越南语独立目录，目前仅登记**第01主题**，73张主卡、4节课。
- `01.json`：完整的第01主题「问候寒暄」，包括73张主卡、替换句、常见回应和66条教学易错说明的越南语版。
- `_translation_notes_01.json`：逐卡教学说明的越南语翻译对照（审核/维护用途，客户端不必下载）。
- `QA_01.json`：源文件和越南语数据的结构及完整性复查结果。

第02–60主题**尚未翻译和发布**。请不要将本目录理解成已完成60主题。

## 正确的中文数据来源

源文件为 `content/interactive-books/talkami_spoken_60/packs/01.json`，源版本 **V13**，Git blob SHA `18749f701488188f5ea265aee15a4cd82bcd5636`。

第01主题原始73张主卡及其中文、拼音、稳定ID、卡片顺序、分级、替换句和回应句全部保留。66条教学说明已翻译；其中原文中12处专讲缅语差异的**中文教学说明**改写成适用于越南学习者的说明，不涉及任何中文练习句的修改。

## 字段兼容

| 缅语数据 | 越南语数据 |
| --- | --- |
| `theme_title_my` | `theme_title_vi` |
| `title_my`, `subtitle_my`, `opening_my` | `title_vi`, `subtitle_vi`, `opening_vi` |
| `lesson_title_my` | `lesson_title_vi` |
| `meaning_my` | `meaning_vi` |
| `mistakes[].text_my` | `mistakes[].text_vi` |

`text`（中文）、`pinyin`、`id`、`level`、`alternatives`、`replies` 等保留原结构。`phonetic_my` 是**缅文近似谐音**，不适合机械转成越南语。越南版只使用原有准确拼音，不生成容易误导读音的“越语谐音”。

**注意：原缅语 App 如果写死读取 `_my` 字段，需要在越南语 App 中改成读取 `_vi`。** 这是独立数据包，不是无需改动客户端代码的直接覆盖包。

## 云端访问

- 独立目录：`https://raw.githubusercontent.com/hurt56631-ui/talkami-learning-content/main/content/interactive-books/talkami_spoken_60/packs/vi/catalog.json`
- 第01主题：`https://raw.githubusercontent.com/hurt56631-ui/talkami-learning-content/main/content/interactive-books/talkami_spoken_60/packs/vi/01.json`

`catalog.json` 的 `public_base_url` 指向原项目根路径；主题 `data_url` 已指向独立的 `packs/vi/01.json`。不要用原缅语 `catalog.json` 加载越南版。

## 复检与质量状态

已逐卡核对主卡和附属句子的中文原文、拼音、编号及顺序；检查了翻译字段非空、JSON结构、重复ID和是否残留缅甸文字。详见 `QA_01.json`。

**越南语内容由 AI 翻译与审校；尚未经过独立越南语母语者最终逐句审校或真人音频测试。** 请在正式商用前进行语言与音频复核。
