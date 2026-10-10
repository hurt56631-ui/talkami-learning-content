# 实用中文口语主题 JSON（单词包式发布）

本目录是 **Talkami 综合口语书** 的新增在线内容入口。保留原版 `web_catalog.json`、`free/*.json.gz.b64` 和 `book_latest.zip`，以兼容已经上线的旧版本。

- 目录：`catalog.json`，10 专区、60 个主题位置；已提供数据的主题含 `data_url`、`data_version`、`data_sha256`、`data_size`。
- 数据包：`packs/01.json` 等，按主题下载。当前 **32 个已发布主题、122 节小课、2140 张主卡片**。其他主题尚未上架，不要虚报为 244 节已完成。
- 格式：`{ "theme_id": "01", "lessons": [{ "id": "01.1", "title": "...", "phrases": [...] }] }`。小课、短句的稳定 ID 不变。
- 主题 01：`01.json` 已采用用户提供的 **v9 · 73 张卡**（教学说明、缅语释义、自然回应、拼音），保留全套 73 个句子 ID。
- 旧版整本 ZIP 是**历史兼容/离线包**，可能不含后续主题新版本；在线阅读优先使用主题 JSON。
- 更新单个主题：保持 `theme_id`、`lessons[].id`、`phrases[].id` 不变；提高数据包 `version` 和目录 `data_version`，同时更新 SHA-256、`data_size`、对应计数及目录顶层版本。
- 网站/APP 收费权益判断继续由客户端结合后台激活状态控制；本仓库公开，JSON 可以公开下载。
