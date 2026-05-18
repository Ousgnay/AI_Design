# XGame Active Session

**current_tool**: codex  
**started_at**: 2026-05-18  
**scope**: ux-collect hero-card molecular batches ingestion, token/style harvesting from Figma component template, organism/molecular knowledge expansion, strict published-component-only harvesting, layout knowledge expansion, and shared-state synchronization  
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
- `decision-source/knowledge/common/layout-decision.md`
- `decision-source/knowledge/common/layout-spec.json`
- `decision-source/knowledge/common/flow-decision.md`
**last_decisions**:
- `ai-shared/` is the only editable shared source
- `AI-workflow-discussion-log.md` is history and changelog only
- `project-status.md` is the current-state source
- `active-session.md` is the handoff source
- `organism_components` and `molecular_components` are now the explicit high-level component entrypoints in shared knowledge
- atom entries remain in original sections for provenance and fallback, not as preferred instantiation entrypoints
- `ia-generate` now prefers `organism_components`, then `molecular_components`, before atom-category fallback during component selection
- Figma `1928:3412`「英雄卡牌」已通过 `ux-collect` 落入 `knowledge/common`
- 本轮新增的武将头像 / 武将列表 / 武将卡牌 / 战法 / HUD头像 / 群头像条目已补齐 `nodeId` 与 `componentKey`
- Figma `5480:6611` 与 `6453:23911` 两批分子层节点已完成补录并写入 `knowledge/common`
- 本轮已新增道具格、武将信息、身份、特技、词条/已学习/限时/自选标签、排名徽章、霸业/赛季标题、勾选行、沙盘底条标签、趋势战况标签、体力标签
- Figma `jB3vJujGbA7pKX9rNIlJUt`「组件 模板 Copy」已完成整文件 style 实采，新增 `tokens-decision.md` 与 `tokens-data.json`
- Figma `1928:3750`「沙盘部队」已完成组织层补录，知识库新增 `organism_components`，消费优先级扩展为 organism > molecule > atom-fallback
- Figma `1928:3790`、`1928:3851`、`5883:5226` 中真实可实例化的组织层组件已完成补录并写入 `knowledge/common`
- Figma `5480:5482`、`1928:3872`、`6194:7817`、`6194:10071`、`6194:10284` 中真实可实例化的组织层组件已完成补录并写入 `knowledge/common`
- Figma `5922:5533` 经核查仅含 frame/instance，无真实顶层 `COMPONENT` / `COMPONENT_SET`，已按规则跳过
- 用户提供的界面分类图已整理写入 `decision-source/knowledge/common/layout-decision.md`
- `ux-collect` 已补齐文件分类约定：`tokens / component / layout / flow`
- `layout-spec.json` 与 `flow-decision.md` 已建立为后续采集入口
- layout 线已明确允许采集 frame 级页面骨架；后续需要在 `layout-spec.json` 中记录 region 级 `x / y / width / height` 与适配信息
- `ux-collect/SKILL.md` 已补充组件分层采集规则：完整业务块优先写入 `organism_components`
- 当前 `ux-collect` 执行额外人工规则：只有真实 `COMPONENT` / `COMPONENT_SET` 且带顶层 `componentKey` 的节点才允许进入高阶组件知识；frame、示例板、场景拼图不录入
- `4832:3245`「中小弹窗」剩余变体已完成补录，并已同步写入 `layout-spec.json` / `layout-decision.md` / `component-spec.json` / `component-decision.md`
- 本轮已确认中小弹窗家族的多个子模式，并将右侧注释继续按横向对应原则映射回左侧实例
- `4884:1889`「中弹窗」已完成整页补录，并已同步写入 `layout-spec.json` / `layout-decision.md` / `component-spec.json` / `component-decision.md`
- 本轮已确认中弹窗家族的搜索列表、双栏阅读、左主视觉右详情、左列表右预览、页签概览和上下复合信息等子模式
- `4970:4432`「大弹窗」已完成整页补录，并已同步写入 `layout-spec.json` / `layout-decision.md` / `component-spec.json` / `component-decision.md`
- 本轮已确认大弹窗家族的左 tab + 中央大列表/空状态、左 tab + 单列/宫格选择区 + 右侧说明栏等子模式
- `4009:327`「满屏浮窗」已完成补录：成功/失败结果层进入 `layout-*`，`名次` 组件集进入 `component-*`
- 本轮已确认满屏浮窗应以“主界面底图 + 压暗层 + 结果横幅 + 排行榜区”的特种 layout 方式处理
- 本轮 layout workflow 已正式固化到共享规则：右侧注释按横向与 `y` 轴邻近映射，家族页先录空白模板再录变体，`component_set` 真实 variant 需单独补 `componentKey`，满屏覆盖层默认 `layout-first`
- repository text policy is now UTF-8 with BOM plus LF for `.md`, `.json`, `.txt`, `.yml`, `.yaml`, `.js`, `.ts`, `.html`, and `.css`
- `decision-source/knowledge/common/component-spec.json` has been normalized to UTF-8 with BOM
- a repeatable read-only encoding audit is now available at `tools/encoding-audit.ps1`
- `ai-shared/docs/project-workflow.md` and `ai-shared/docs/path-registry.md` now explicitly route future text-file work through the BOM policy and audit entry point
**next_step**:
- continue ingesting the next user-provided layout or flow URLs
- verify `ia-generate` can directly consume the newly harvested organism components and layout templates in a real planning case
**open_risks**:
- some tool integrations may still assume local skill bodies instead of following shim references
- `.claude/settings.local.json` still contains historical private-path references by design
- future structural changes must respect the new approval-before-log rule
- Windows PowerShell 5.1 default display behavior can still misrender UTF-8 unless reads are explicit UTF-8
- scene-style Figma boards may visually resemble organisms but still fail the published-component rule and must be skipped
**handoff_ready**: true

---

> 本文件只记录当前轮交接状态。切换 Codex / Claude 前先更新这里。
