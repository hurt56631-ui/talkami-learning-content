# Talkami 实用中缅词典 V5：16 大类、163 小类、4500 词

**2026-11-05 再更新：01–08 类现有 1–2 条中缅双语例句；09–16 类仍仅有词目。所有实用分类均不含搭配，原 HSK1–4 词包不变。**

*以下“首次发布”“第五轮”等段落是 2026-11-02 的历史记录，最新状态请以末尾更新说明为准。*

## 词条结构
每条词保留标准 HSK JSON 相容字段：`id, hanzi, pinyin, phonetic_my, burmese, collocations, collocations_pinyin, collocations_my, collocation_ids, examples, level`，新增 `category_id, category, subcategory_id, subcategory, source_order, content_status`。

- 4500 条中缅四列词目完整保存；每个词均有唯一稳定的 **ID 1000001–1004500**。
- 按 **16** 大类、**163** 小类，逐条保留源词顺序来源。
- 首次发布时为节省配音，**4500 词均无例句和搭配**（`dictionary_only`）；2026-11-05 已为 01–04 类加入纯文字例句（`examples_ready`），所有搭配仍为空，05–16 类仍为 `dictionary_only`。
- 语音建议只给词目中文配 1 条；**本次未生成音频文件**。
- 从原 V4 完成 86 条分类迁移、5 处小类名称修正、6 处拼音修正、11 处缅语多义词或释义补充，详见 audit。
- 对于 `WiFi`、`U盘`、`T恤` 这类混合字母的词，实际 TTS 朗读应先听测，不宜直接假设发音正确。

## 16 个分类

| 编号 | 分类 | 词条数量 | 小类数量 |
|---|---|---:|---:|
| 01 | 基础中文与交流 | 225 | 9 |
| 02 | 数字时间与方位 | 378 | 9 |
| 03 | 人物家庭与身份 | 137 | 3 |
| 04 | 饮食食材与餐饮 | 350 | 13 |
| 05 | 居家生活与日用品 | 250 | 8 |
| 06 | 衣服穿戴与个人护理 | 195 | 6 |
| 07 | 购物金钱与物流 | 291 | 14 |
| 08 | 交通出行与地点 | 254 | 10 |
| 09 | 工作求职与工厂 | 467 | 25 |
| 10 | 身体健康与医疗 | 254 | 6 |
| 11 | 学习语言与教育 | 221 | 7 |
| 12 | 手机网络与数码 | 180 | 7 |
| 13 | 社交情绪与休闲 | 239 | 12 |
| 14 | 办事证件与安全 | 184 | 13 |
| 15 | 自然天气与动植物 | 108 | 8 |
| 16 | 常用动作与描述 | 767 | 13 |

**合计：4500 词，16 大类、163 小类。**

## 文件位置

- `content/words/packs/practical_16_v5/category_01.json` 至 `category_16.json`
- `content/words/practical_16_v5_catalog_draft.json`：分类目录历史草案；正式入口已接入 `content/words/catalog.json`
- `content/words/practical_16_v5_audit.json`：逐词的最终原分类到当前分类变更记录、拼音/释义修订、复核注意事项

## 发布注意

1. `level: "practical"` 表示实用词典，不是 HSK 官方考试等级。
2. 前端需要容忍 `collocations: []` 和 `examples: []`；上线前测试词典卡片、类别跳转及异体字/英文缩写配音。
3. 4500 条缅语释义来自用户精校 V4，只有定向修正；**仍未通过缅语母语老师全部逐条终审**，不得宣传 100% 无误。
4. 词库目录与 16 张封面已合并到 main，Release content-v1.6.40 已正式发布；仍需在 App 端确认目录刷新、词卡和中文 TTS。

## 第三轮优化：最小配音与目录接入检查

- 建议优先使用 App 的中文 TTS（`zh-CN`）即时朗读 `hanzi`。因此不必提前录制 4500 个 MP3；词目以外不需要任何配音。
- 需要批量录音时，使用 `content/words/practical_16_v5_audio_words_only.csv` 的 **4500** 个独立词目（包含稳定 ID、中文词目、拼音、原分类调整后的分类、建议文件名、TTS 待试听标志）。本次没有生成或上传音频。
- `WiFi`、`U盘`、`T恤`、`喂` 和 `血` 的读音需特别试听；其他词也不能保证 TTS 自动朗读毫无偏差。
- `scripts/build_release.py` 的 `safe_asset_name` 仅接受文件名，原目录草案里的 `practical_16_v5/category_XX.json` **不能用作 Release 的 data_url**。现已改为 `talkami-practical-XX-v5.json`。源码 JSON 仍放在 `practical_16_v5/category_XX.json`，由发布器打包输出为平铺资源。
- 已补齐 16 张独立 PNG 分类封面；正式 catalog.json 已增加 16 个入口。已成功发布 content-v1.6.40；仍需在 App 检查分类加载。
- 原 HSK1–4 的词包未作修改，正式目录以新增入口方式升级；本次只接入实用词词典，不给 HSK 文件增加或删除例句。

## 第四轮：16 张封面与正式目录接入（2026-11-02）

- 新增 `content/words/covers/practical_01.png` 至 `practical_16.png` 16 张独立彩色封面：统一视觉体系、不同编号、不同主题图标。图片不含自动生成的缅语文字，避免错别字；词卡标题由目录 `title` 字段显示。
- `content/words/catalog.json` 的版本从 6 提升到 7，保留原 3 个 HSK1–3 旧版入口并追加 16 个 `practical_XX` 实用词典入口（总计 19 个）。
- 每个新入口有 `cover_url`、`cover_version: 1`、`source_cover`、`data_url`、`data_version: 2`、`level`、`source_data`，可由 `scripts/build_release.py` 处理。
- 新词典共 4500 条，严格不含搭配、例句。封面 PNG 作为配图，词目可以使用 App 中文 TTS；没有新增任何录音文件。
- **合并仓库 ≠ 发布应用内容**：需在 GitHub Actions 的 `Publish learning content` 触发新 Release 版本（如 `1.6.40`；使用前检查该版本未占用），验证 `words-catalog.json` 和 16 对分类数据包/封面均在新 Release 中，再在 App 中打开分类进行实测。
- 源词典未经缅语母语老师全部 4500 条逐词终审，本次主要完成数据质量与接入路径校验。

## 第五轮：正式内容发布验收

- **2026-11-02 已发布**：[content-v1.6.40](https://github.com/hurt56631-ui/talkami-learning-content/releases/tag/content-v1.6.40)，官方 Publish learning content 工作流状态为 success。
- Release 总计 **147** 个资源文件；已核对 16 个 `talkami-practical-XX-v5.json` 与 16 个 `talkami-practical-XX-cover-v1.png` 全部存在，无缺失。
- `words-catalog.json` 以及旧版 HSK1、HSK2、HSK3 数据包都在 Release 中，兼容原有词库入口。
- 为修复历史 HSK2 搭配检测误报，将发布器中中文和缅文字元范围正则的双反斜杠改为单反斜杠，保留 HSK 词包数据原样；增加 HSK2/3 原发布器回归检查。
- 本次发布没有新增音频文件，实用词只需中文词目 TTS；搭配和例句为零。
- 一次性发布调度 workflow 已在后续清理提交中删除，今后应按仓库常规工作流手动指定新的 Release 版本。
- **尚未在用户设备上完成 Talkami App 实测**；需确认 App 的远程 Release 基础 URL、缓存刷新、16 个分类卡片、空搭配例句、词目音频朗读是否正常。

## 第六轮：01–04 分类补充文字例句（2026-11-05）

- 按用户要求，**只增加例句，不增加搭配**；无音频或配音文件。
- 分类 01 基础中文与交流：225 词 / 299 例句。
- 分类 02 数字时间与方位：378 词 / 594 例句。
- 分类 03 人物家庭与身份：137 词 / 213 例句。
- 分类 04 饮食食材与餐饮：350 词 / 413 例句。
- 总计 1090 词 / 1519 例句，每词 1–2 条；例句有 `id`, `hanzi`, `pinyin`, `burmese`，未改词目 ID、音标、释义、类别；所有搭配字段继续为空。
- HSK1–4、分类 05–16 未修改；第 01–04 类目录升级到 `data_version: 3`，数据资源名改为 `talkami-practical-01-v6.json` 至 `talkami-practical-04-v6.json`，目录 `version: 8`。
- 句子优先复用已有 HSK 双语例句，缺失内容按生活场景补充。新编缅语翻译仍需母语教师逐条人工终审，不应声称已 100% 精校。
- **此次仅为 GitHub 源文件更新**；必须运行 Publish learning content 发布新的 Release，才能让 App 获取更新。

## 第七轮：05–08 分类补充文字例句（2026-11-05）

- 05 居家生活与日用品：250 词 / 277 例句。
- 06 衣服穿戴与个人护理：195 词 / 218 例句。
- 07 购物金钱与物流：291 词 / 320 例句。
- 08 交通出行与地点：254 词 / 332 例句。
- **本批共 990 词 / 1147 例句；01–08 共 2080 词 / 2666 例句**。每词 1–2 条，附例句 ID、中文、拼音、缅文。
- 不修改词目、稳定 ID、四列释义或原有分类；不增加搭配、不制作例句或搭配配音；09–16 分类仍无例句。
- 目录版本升级至 9，05–08 词包资源名为 `talkami-practical-05-v6.json` 至 `talkami-practical-08-v6.json`，`data_version: 3`。
- 格式及数量可由 `scripts/check_practical_word_packs.py` 检查；语言内容的最终质量仍需缅语母语教师及拼音精校人员审核。
- 合并到 main 并不代表发布到客户端：需要单独发布新的 GitHub Release 并进行 App 端验收。
