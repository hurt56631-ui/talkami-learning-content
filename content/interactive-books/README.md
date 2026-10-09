# 实用中文口语 · 互动书籍目录

本仓库用于公开展示书籍/口语专题：封面、书名、目录、前30句免费数据和按版本发布的完整章节 ZIP。目录：`content/interactive-books/catalog.json`。

## 服装厂中文1000句 v1.7

- 书籍 ID（永久不变）：`garment_factory_1000`
- 完整 ZIP：`content/interactive-books/garment_factory_1000/book_latest.zip`
- 历史存档：`content/interactive-books/garment_factory_1000/archive/garment_factory_1000_v1_7.zip`
- 网页目录：`content/interactive-books/garment_factory_1000/web_catalog.json`
- 免费30句：`content/interactive-books/garment_factory_1000/free_preview.json`
- Android 目录片段：`content/interactive-books/garment_factory_1000/android_catalog_fragment.json`

完整 ZIP **公开可下载**，这是内容方确认的发行选择。登录、激活码、书籍 VIP **只能限制 Talkami 网站内使用权限，不能阻止直接访问 GitHub 的 ZIP**；请不要将公开 ZIP 误称为保密或受 DRM 保护的资源。

### 今后更新同一本书

1. 保持商品 ID `garment_factory_1000` 和全部稳定短句 ID 不变，保留11章编号结构（现有网站/后端仍使用固定11章）。
2. 更新 `book_latest.zip` 与归档副本，必要时更新网页目录、前30句、Android目录。
3. 更新 `catalog.json` 的 `content_version`、`bundle_sha256`、`bundle_size`。ZIP 下载时服务器会核对大小、SHA-256 和11章/1000句结构；校验失败会拒绝新数据。
4. 对网站的免费30句/场景目录若有修改，仍需同步部署网站静态资源，避免浏览器浏览到旧目录。
5. 本书缅语译文与缅语谐音仍在等待缅甸籍服装厂教师终审。数据结构校验不等于语言质量认证。

### 增加新口语专题

在 `catalog.json` 的 `items[]` 里追加稳定的 `id`、`type:"book"`、`status:"active"`、`title`、`item_count`、`free_count`、`content_version`、`sort_order` 和可选 `cover_url`。后台「用户权限」约五分钟自动读取新目录，也可手动强制刷新，实现按 UID 授权。

**注意：新增新书元数据会自动出现在授权后台，但不会自动获得一个兼容的网页目录/ZIP阅读器。** 完整上架还需要对应的前端通用书籍加载器和数据包标准。

App 的其它单词/口语数据继续使用各自 `content/words`、`content/speaking` 等目录，普通 PDF 的 `content/books` 也不受影响。
