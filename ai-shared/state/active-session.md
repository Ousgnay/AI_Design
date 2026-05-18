# XGame Active Session

**current_tool**: codex  
**started_at**: 2026-05-18  
**scope**: ux-collect hero-card molecular batches ingestion, molecular-component knowledge expansion, and shared-state synchronization  
**files_in_play**:
- `AI-workflow-discussion-log.md`
- `ai-shared/state/project-status.md`
- `ai-shared/state/active-session.md`
- `ai-shared/skills/ia-generate/SKILL.md`
- `ai-shared/docs/collaboration-protocol.md`
- `ai-shared/docs/encoding-governance.md`
- `.editorconfig`
- `.gitattributes`
- `tools/encoding-audit.ps1`
- `decision-source/knowledge/common/component-decision.md`
- `decision-source/knowledge/common/component-spec.json`
**last_decisions**:
- `ai-shared/` is the only editable shared source
- `AI-workflow-discussion-log.md` is history and changelog only
- `project-status.md` is the current-state source
- `active-session.md` is the handoff source
- `molecular_components` is the only explicit molecule-layer entrypoint in shared knowledge
- atom entries remain in original sections for provenance and fallback, not as preferred instantiation entrypoints
- `ia-generate` now prefers `molecular_components` before atom-category fallback during component selection
- Figma `1928:3412`「英雄卡牌」已通过 `ux-collect` 落入 `knowledge/common`
- 本轮新增的武将头像 / 武将列表 / 武将卡牌 / 战法 / HUD头像 / 群头像条目已补齐 `nodeId` 与 `componentKey`
- Figma `5480:6611` 与 `6453:23911` 两批分子层节点已完成补录并写入 `knowledge/common`
- 本轮已新增道具格、武将信息、身份、特技、词条/已学习/限时/自选标签、排名徽章、霸业/赛季标题、勾选行、沙盘底条标签、趋势战况标签、体力标签
- repository text policy is now UTF-8 with BOM plus LF for `.md`, `.json`, `.txt`, `.yml`, `.yaml`, `.js`, `.ts`, `.html`, and `.css`
- `decision-source/knowledge/common/component-spec.json` has been normalized to UTF-8 with BOM
- a repeatable read-only encoding audit is now available at `tools/encoding-audit.ps1`
- `ai-shared/docs/project-workflow.md` and `ai-shared/docs/path-registry.md` now explicitly route future text-file work through the BOM policy and audit entry point
**next_step**:
- run a Phase 1 end-to-end validation with a real planning document
- verify `ia-generate` can directly consume the newly补录的英雄卡牌分子组件条目 in a real planning case
**open_risks**:
- some tool integrations may still assume local skill bodies instead of following shim references
- `.claude/settings.local.json` still contains historical private-path references by design
- future structural changes must respect the new approval-before-log rule
- Windows PowerShell 5.1 default display behavior can still misrender UTF-8 unless reads are explicit UTF-8
**handoff_ready**: true

---

> 本文件只记录当前轮交接状态。切换 Codex / Claude 前先更新这里。
