# Talkami Learning Content 远程内容仓库

这个仓库用于给唐僧叨叨二开的学习模块发布：

- 单词目录、单词包和单词封面
- 口语短句目录和短句包
- 学习路径目录和课程 ZIP

App 的正常流程是：

1. 在线读取很小的目录 JSON。
2. 目录发现新分类或更高的数据版本。
3. 用户打开对应分类时，App 下载数据包。
4. 数据通过 SHA-256 校验后保存到手机本地。
5. 之后从本地读取；断网时继续使用缓存或 APK 内置内容。

## 当前内容

### 单词：HSK1–HSK3 共 600 个

- HSK1 基础词汇：150 个
- HSK2 基础词汇：150 个
- HSK3 基础词汇：300 个

各单词包都包含中文、标准拼音、缅语释义、缅语近似谐音和中缅双语例句。网页会在需要时生成例句拼音。缅语谐音仅供发音入门，不能代替标准拼音与中文录音。原“工作办公”词包仅作历史归档，不再展示在学习目录。

### 口语：81 句

- 日常交流：15 句
- 旅行问路：20 句，数据版本 2
- 酒店入住：12 句
- 餐厅点餐：12 句
- 购物付款：12 句
- 紧急求助：10 句

## 发布新内容

1. 修改 `content/` 中的源文件。
2. 打开 GitHub 仓库的 `Actions`。
3. 运行 `Publish learning content`。
4. 输入一个从未使用过的新 Release 版本，例如 `1.1.0`。
5. 工作流会：
   - 检查 JSON 格式
   - 检查重复 ID
   - 检查目录和数据包 ID 是否一致
   - 检查必填中文、拼音和缅语释义
   - 计算 SHA-256
   - 统计单词或短句数量
   - 生成完整 `dist/`
   - 发布新的 GitHub Release

每个最新 Release 都会包含全部当前资源，不是只包含本次改动，因此 `/releases/latest/download/` 下的所有地址都能继续使用。

## 单词维护

目录：

`content/words/catalog.json`

数据包：

`content/words/packs/*.json`

封面：

`content/words/covers/*.webp`

修改已有单词包时：

- 保持目录 `id` 和词包 `categoryId` 不变
- 保持已有单词 `id` 不变
- 提高词包根部 `version`
- 换一个带新版本的文件名
- 同步修改目录中的 `data_url`、`data_version` 和 `source_data`
- 只改封面时提高 `cover_version`，并修改 `cover_url` 与 `source_cover`

新增整个单词分类时：

- 新建一个词包 JSON
- 新建一张 WebP 封面
- 在 `content/words/catalog.json` 中新增一个叶子节点
- 目录 `level` 必须等于词包 `categoryId`

脚本会自动填写最终目录中的 `data_sha256` 和 `item_count`。

## 口语维护

目录：

`content/speaking/catalog.json`

短句包：

`content/speaking/packs/*.json`

修改已有口语包时：

- 保持目录叶子节点 `id` 和短句包 `pack_id` 不变
- 保持已有短句 `id` 不变
- 提高短句包 `version`
- 换一个带新版本的文件名
- 同步修改目录中的 `data_url`、`data_version` 和 `source_data`

新增口语包时：

- 新建一个短句包 JSON
- 在 `content/speaking/catalog.json` 的相应 `children` 中新增叶子节点
- 目录叶子节点 `id` 必须等于短句包 `pack_id`

当前口语卡片不使用远程封面，所以无需上传口语封面。

## Android 地址

Android 项目的：

`wklearning/src/main/assets/learning/config/remote_content.json`

应配置为：

`https://github.com/hurt56631-ui/talkami-learning-content/releases/latest/download/`

并读取：

- `words-catalog.json`
- `speaking-catalog.json`
- `learning-path-catalog.json`

仓库必须保持 Public。不要把 GitHub 私人 Token 写入 APK。

## 重要版本规则

有三类版本：

- GitHub Release 版本：每次运行 Actions 输入新值，例如 `1.1.0`
- 数据包版本：只有修改对应单词包或口语包时才增加
- 封面版本：只有更换单词封面时才增加

不要复用旧 Release 版本，也不要修改已有内容的稳定 ID。


### 4500 实用中缅词典（2026-11-02）

最新 [content-v1.6.40](https://github.com/hurt56631-ui/talkami-learning-content/releases/tag/content-v1.6.40) 已增加 16 个实用主题词分类、4500 个词目和 16 张独立封面。首次发布的实用词典不含例句与搭配；2026-11-05 已在内容源码中为第 01–04 类共 1090 个词新增 1519 条文字双语例句，仍不含搭配和新增音频；第 05–16 类保持原样。需发布新的 Release 后 App 才能获取这项更新。HSK 旧版 600 词原内容保留。若 Android 项目还使用原所有者 Hurt6465-ai 的远程 URL，建议改为当前规范的 `hurt56631-ui` Release 地址，并刷新线上词库目录缓存。

### 实用词分类 01–04：2026-11-05 例句补充

- 第 01 类：225 词、299 例句；第 02 类：378 词、594 例句；第 03 类：137 词、213 例句；第 04 类：350 词、413 例句，共 1519 条。
- 每词保留原词目 ID 和中文/拼音/缅文原释义，新增 1–2 条含 ID、中文、拼音、缅文的例句；**没有搭配**。
- 目录版本 `8`；第 01–04 类资源由 `talkami-practical-0X-v5.json` 升级为 `talkami-practical-0X-v6.json`，对应 `data_version: 3`；其余分类和 HSK 不改。
- 此处源代码更新并不等于线上 Release 已更新；需要通过 Actions 发布新的版本。
