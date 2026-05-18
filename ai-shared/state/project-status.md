# XGame Project Status

**last_updated**: 2026-05-18  
**last_change_ref**: `decision-source/knowledge/common/component-decision.md` / `component-spec.json` 英雄卡牌分子层两批补录

---

## Current Phase

Phase 1 - 核心流验证推进中

---

## Current Todo

- 验证真实策划文档的端到端 IA 输出
- 确认 `ux-collect` -> `ia-generate` -> Figma 的衔接路径
- 保留 Phase 2 / Phase 3 议题，等 Phase 1 验证完成后再推进

---

## Blockers

- Phase 1 端到端验证尚未完成

---

## Next Step

- 运行一个真实策划需求，通过 `ia-generate` 产出 IA 文档并人工复核
- 验证 `ia-generate` 已按 `molecular_components -> atom fallback` 顺序输出组件清单
- 用 Claude / Codex 各做一次共享入口读取，确认不再依赖旧正文

---

## Notes

- 当前共享知识源已显式区分原子层与分子层，`molecular_components` 是分子组件唯一显式入口
- 本轮已完成分子优先实例化规则落地，并已获人类批准同步写入项目日志
- `ia-generate` 已补充分子优先消费策略：先读 `molecular_components`，原分类仅作原子兜底
- 已完成一次新的 `ux-collect` 实采：Figma「英雄卡牌」(`1928:3412`) 已补录到 `knowledge/common/`
- 本次新增武将头像、武将列表卡、武将大卡、战法卡、HUD头像、群头像等分子组件条目，且已补齐 `componentKey`
- 已继续完成 Figma「英雄卡牌」分子层第 1/2 批补录：`5480:6611` 与 `6453:23911` 已写入 `knowledge/common/`
- 本次补录扩展了道具格、武将信息、身份、特技、状态标签、排名徽章、地图标题、勾选行、趋势标签、体力标签等分子组件
- repository encoding baseline verified: 25 target text files are strict UTF-8 and all target files now carry UTF-8 BOM by policy
- repository encoding policy is documented in `ai-shared/docs/encoding-governance.md` and enforced for common text types via `.editorconfig` and `.gitattributes`
- read-only encoding audit entry point is `tools/encoding-audit.ps1`; in Windows PowerShell 5.1, inspect text with explicit UTF-8 reads
- shared workflow entry documents now explicitly require future text files to follow UTF-8 with BOM + LF and route encoding checks through `tools/encoding-audit.ps1`
- 历史背景与结构变更过程见 `AI-workflow-discussion-log.md`
