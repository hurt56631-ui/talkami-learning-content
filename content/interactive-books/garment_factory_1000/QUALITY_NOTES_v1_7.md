# 服装厂中文1000句 · v1.7 数据复核

日期：2026-10-09。此记录针对本次公开发布包（不涉及以前的 v1.2 付费包）。

## 已由程序核对

- 11章，每章独立 JSON；40个真实场景，共1000个句子，编号1—1000连续。
- 主句 `id` 唯一，无完全相同的中文主句。
- 所有1000句均包含中文、拼音、缅文谐音、缅语释义、使用说明、回应、类似说法、拆解。
- 1904条回应、1003条类似说法、2816个词组拆解。
- 网页目录的各场景数量与主句的 `scene_id` 分布完全对应。
- 免费30句与整包前30句内容相同。
- 完整包仅11个预期 JSON 文件，SHA-256 和大小与公开目录一致；存档文件与当前版本一致。
- 网站的短句卡片解析器已经支持 `breakdown`、`phonetic_my`、`replies`、`alternatives`、`when_to_use_my`。

## 本次修复

- 第722句的类似说法：拼音 `yǒu méi yǒu nǎ dào gōng xù? lòu zuò?` 修为 `yǒu méi yǒu nǎ dào gōng xù lòu zuò?`。
- 第845句的一个回应：拼音 `hái chà jǐ jiàn? méi dēng jì.` 修为 `hái chà jǐ jiàn méi dēng jì.`。

主句及句子编号没有改动，已有主句配音不需要因为上述两处改动而重新制作。

## 尚未取得的语言认证

原数据明确标注 `meaning_my_status=manual_draft_needs_native_review` 和 `phonetic_my_status=rule_based_draft_needs_native_review`。自动检查只能证明字段完整和结构正确，**不能证明所有缅语翻译、缅文谐音、服装专业术语都符合缅甸籍工人真实口语**。正式大量销售前仍建议请缅甸籍服装厂教师重点抽查及复核。

## 发布方式与限制

本书的教学 ZIP 根据内容方授权**公开存于 GitHub**。需要知道完整 ZIP 可从仓库直接下载；本网站的账号 VIP 授权并不是防复制保护。以后教材更新时须同步更新 `catalog.json` 中的 `bundle_sha256` 和 `bundle_size`，通过 `scripts/check_interactive_books.py` 的验证后再发布。
