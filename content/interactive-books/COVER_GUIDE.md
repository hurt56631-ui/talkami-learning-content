# 互动口语教材封面使用说明

封面存放在本仓库 `content/interactive-books/covers/`，与实际收费 ZIP 完全分开。上传/替换封面图片不需要更新服务器 Docker。

## 上架封面

1. 推荐尺寸：**600 × 800 像素**或等比例 **3:4**；建议 WebP，文件尽量不超过 200 KB。
2. 命名为稳定的商品 ID，如 `garment_factory_1000.webp`、`restaurant_chinese_500.webp`。
3. 在 `content/interactive-books/catalog.json` 中找到相应 `id` 的书籍，设置：
   `"cover_url": "https://raw.githubusercontent.com/hurt56631-ui/talkami-learning-content/main/content/interactive-books/covers/garment_factory_1000.webp"`
4. 提交到 `main`。前台书架使用图片标签自动渲染封面；图片加载失败时保留文本样式的备用封面。
5. 保持图片封面与书籍 ID 对应。换内容只需更新图片文件；为了绕开设备缓存，也可使用新文件名（例如 `garment_factory_1000_v2.webp`）并更新 `cover_url`。

当前已包含 SVG 演示封面 `garment_factory_1000.svg`，今后可以直接换成真实的服装厂摄影封面。**SVG 也是浏览器可显示的图片**。

## 部署注意

GitHub 源仓库公开。所有图片和原始教材 ZIP 都可以从仓库直链访问，VIP 只控制站内阅读。少量图文可从 `raw.githubusercontent.com` 读取，用户多时建议缓存到 Cloudflare/R2 或通过受控 CDN 域名分发，避免把 GitHub Raw 当作无限量商业 CDN。
