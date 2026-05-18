# XGame AI 设计工作流 — 架构决策日志

---

## §0 元信息

| 项 | 值 |
|---|---|
| 项目代号 | XGame |
| 游戏类型 | 手游 SLG（率土之滨 like；竞品：三国谋定天下、率土之滨） |
| 核心定位 | 信息生成，不是图像生成 |
| 当前 Phase | Phase 1 — 核心流搭建中 |
| 本文档位置 | [项目根]/AI-workflow-discussion-log.md |
| 初始版本日期 | 2026-05-15 |

---

## §1 架构决策（D 编号体系，只增不删）

> 格式：**编号 — 结论**  
> 背景：为什么这样决定  
> 影响范围：哪些文件/Skill 受约束

---

### D1 — 从 TGame 全量清空重建，不做渐进迁移

**背景**：XGame 是从 TGame 手动拷贝并只对根目录重名的项目，所有内部路径、Skill 逻辑仍引用 TGame 资产，存在 4 个 BLOCKER 级矛盾。渐进迁移比全量重建风险更高。  
**影响范围**：.claude/skills/ 全部旧 Skill 目录已删除；figma-design-spec/、web-prototype/、audit-reports/ 等 TGame 遗留目录已删除。

---

### D2 — 核心定位：信息生成，不是图像生成

**背景**：XGame 是 SLG，界面信息密度高、业务逻辑复杂。AI 应专注于"从业务逻辑推导出结构化 IA"，而非"描述一张图让 AI 画"。  
**影响范围**：所有 Skill 的设计方向；ia-generate 的输出是结构化 MD 文档，不是 Figma 指令。

---

### D3 — 流程链：业务逻辑 → 信息架构 IA → 信息实例化 → 自我学习

**背景**：4 个环节对应 4 个角色：策划提供业务逻辑，AI 推导 IA，官方 Figma Skill 实例化，self-improving 持续迭代。  
**影响范围**：整体工作流顺序；环节之间的产物定义。

---

### D4 — decision-source/ 置于项目根，作为中立共享知识库

**背景**：ux-collect、ia-generate、self-improving 三个 Skill 都需要访问 knowledge/ 和/或 learnings/，但各有不同权限。将知识库归属于任何一个 Skill 都会制造路径耦合。放在项目根、由 CLAUDE.md 统一注册路径，是最干净的解决方案。  
**影响范围**：decision-source/ 路径；CLAUDE.md 路径注册；所有 Skill 内部禁止硬编码 decision-source 路径。

---

### D5 — 权限矩阵：Skill 对 decision-source/ 的读写权限

| Skill | knowledge/ | learnings/ |
|---|---|---|
| ux-collect | ✍️ 读写 | — 无权限 |
| ia-generate | 👁 只读 | 👁 只读 |
| self-improving | ✍️ 读写 | ✍️ 读写 |
| workflow-auditor | 👁 只读（Phase 3 待定） | 👁 只读（Phase 3 待定） |
| unity-csharp-spec | 👁 只读（Phase 3 待定） | — 无权限（Phase 3 待定） |

**背景**：ux-collect 采集规则写入 knowledge/；ia-generate 纯读用于推理；self-improving 需要读写两者以实现学习闭环。  
**影响范围**：各 SKILL.md 的权限声明；AI 执行时不得越权操作。

---

### D6 — 官方 Figma Skill 包不做硬约束，按需组合

**背景**：环节3（信息实例化）需要 figma-generate-design / figma-use / search-design-system MCP 等多个工具协作，强制指定单一 Skill 会限制灵活性。用户手动触发，AI 根据任务决定调用哪些工具。  
**影响范围**：ia-generate SKILL.md 中的"下游说明"；不建立 figma-generate-design 依赖声明。

---

### D7 — 三阶段验证：Phase 1 核心流 → Phase 2 学习闭环 → Phase 3 配套工具

**背景**：主干先验证，问题早暴露；学习闭环在核心流稳定后接入；workflow-auditor 和 unity-csharp-spec 范围尚未明确，留到 Phase 3 单独讨论。  
**影响范围**：构建顺序；Skill 骨架的完成时间表。

---

### D8 — Phase 1 验证标准：三个评估点，均达"可接受"方为通过

**背景**：Figma 界面产出质量是 Phase 1 的核心验证指标，需要从 IA 文档质量、布局准确性、Component 引用准确性三个维度人工评估。  
**影响范围**：Phase 1 出口条件；测试用例选择。

评估点：
- 评估点 1：决策源 → IA 文档质量（ia-generate 产出是否准确反映业务逻辑）
- 评估点 2：Layout 准确性（容器选择、信息层级、布局区划）
- **评估点 3：Component 引用准确性（能复用的是否正确引用，尤其是 component）**

---

### D9 — Phase 2 验证标准：同一需求重跑，bad case 有明显减少

**背景**：学习闭环的价值在于"越用越聪明"，用同一个 Phase 1 的测试需求重跑并对比，是最直接的验证手段。  
**影响范围**：Phase 2 出口条件；bad case 记录规范（记入 learnings/pending/）。

---

### D12 — ux-collect 新增 Design Token 采集能力

**背景**：Figma Design System 的 token 变量（颜色、间距、字号、圆角等）是 ia-generate 进行界面规范判断的基础数据。将 token 采集纳入 ux-collect 工作流，产出 `tokens-decision.md`（使用规范）和 `tokens-data.json`（原始数据），ia-generate 在 always-loaded 阶段同步读取。  
**影响范围**：ux-collect/SKILL.md 步骤1 + 文件选择；ia-generate/SKILL.md always-loaded 列表；knowledge/common/ 新增两个文件。

---

### D11 — 每个 SKILL.md 必须包含 YAML frontmatter + 500 行约束

**背景**：frontmatter（name / description / disable-model-invocation）是 Claude Code Skill 系统的规范格式，缺少会导致 Skill 无法被正确识别和描述。500 行上限防止单个 SKILL.md 膨胀为难以维护的巨型文档；超限时必须经人工审批才能写入，避免 AI 自行堆砌内容。  
**影响范围**：所有 SKILL.md 文件；未来新增或扩充 SKILL.md 时必须遵守此规范。

---

### D10 — CLAUDE.md 统一路径注册，Skill 内部禁止硬编码跨 Skill 路径

**背景**：路径集中管理才能保证重构时改一处生效，避免 TGame 时代的"每个 Skill 各自硬编码路径"导致的不一致问题。  
**影响范围**：CLAUDE.md 路径注册章节；所有 SKILL.md 的路径引用方式（用注释说明"路径由 CLAUDE.md 注册，见 §跨Skill路径注册"）。

---

### D13 — nodeId 存入 component-spec.json，打通 ia-generate → 官方 Figma Skill 直链

**背景**：ia-generate 推理出具体组件后，下游官方 Figma Skill 若通过 `search_design_system` 重新检索，会重复消耗 token 遍历 design system。通过 ux-collect 采集时一并存储每个组件的 Figma nodeId，ia-generate 在 Component 清单中携带 nodeId 输出，官方 Figma Skill 可直接调用 `get_design_context(nodeId)` 精准定位，实现零重复遍历。  
**nodeId vs componentKey 取舍**：componentKey 更稳定但 MCP 工具不直接接受，需额外转换；nodeId 所有 MCP 工具直接支持，设计系统大幅重建时本来就需要重跑 ux-collect，nodeId 届时同步刷新，稳定性风险可接受。  
**影响范围**：ux-collect/SKILL.md 步骤1（采集时记录 nodeId）；ia-generate/SKILL.md 输出格式（Component 清单加 nodeId 列）；component-spec.json schema（每条目加 `nodeId` 字段，meta 加 `last_synced`）。

> **D14 补注（2026-05-15）**：D13 取舍部分"componentKey 不直接接受"描述不完整——componentKey 是 `use_figma` 实例化 Library 组件的唯一路径，nodeId 与 componentKey 用途不同、互不可替代，见 D14。

---

### D14 — componentKey 同步采集，use_figma 实例化 Library 组件的唯一路径

**背景**：Phase 1 验证暴露：ia-generate 只输出 nodeId，但 `use_figma` 中 `figma.importComponentByKeyAsync()` 需要 componentKey（组件发布 UUID）。`figma.getNodeById(nodeId)` 只在当前文件内查找，无法找到跨文件 Library 组件。nodeId 和 componentKey 用途不同、互不可替代：nodeId 供 MCP 读取工具（get_design_context / get_screenshot）精准定位；componentKey 供 use_figma 将 Library 组件实例化到画布。  
**取值方法**：在源库文件（`jB3vJujGbA7pKX9rNIlJUt`）执行 `use_figma`，对每个 COMPONENT 节点读取 `node.key` 即得 componentKey。已批量采集 25 个组件，写入 `component-spec.json` 的 `meta.componentKeys` 查找表。  
**附加发现**：「组件&模板 (Copy)」为部分发布库，5 个组件（btn_c_lv1_normal_1/2、bg_c_boxblock_07/灰、btn_c_fanhui）需在 Copy 源文件中 Publish 后方可实例化。  
**影响范围**：ux-collect/SKILL.md 步骤1（组件库采集增加 componentKey 采集步骤）；ia-generate/SKILL.md Component 清单格式（加 componentKey 列）；component-spec.json schema（meta 加 componentKeys 查找表）。

---

### D15 — search_design_system 对本项目 team library 不可检索，组件发现依赖 component-spec.json

**背景**：Phase 1 验证暴露：`search_design_system` 对 team library「组件&模板 (Copy)」始终返回空（即使传入正确 `includeLibraryKeys` 也无效）。该工具只对公开/社区库可靠。错误使用会把无关项目的 DS 混入结果，产生噪声。  
**结论**：**默认禁止** AI 自行将 `search_design_system` 用于本项目组件发现；`component-spec.json`（nodeId 供 MCP 定位，componentKey 供实例化）是默认权威来源。若用户明确指示"用 search_design_system 搜索"，则可执行，但需在结果中标注来源库并过滤掉与本项目无关的外部 DS 噪声。  
**影响范围**：ux-collect/SKILL.md 步骤1（search_design_system 加默认禁用警告）；ia-generate/SKILL.md 下游衔接（去除 search-design-system 正面引用，加注释说明默认禁用但可人工开启）。

---

### D16 — componentKey 字段下沉到各 component 条目，废弃 meta.componentKeys 查找表设计

**背景**：D14 计划将 componentKeys 写入 `meta.componentKeys` 查找表，但数据从未实际填入（文件中只有 `_note_componentKeys` 注释）。Phase 1 验证（Figma MCP 查 Node 7039:52722 即 `slg_city_label_faction`）确认：COMPONENT_SET 的每个变体是独立 COMPONENT，各有自己的 key；`figma.importComponentByKeyAsync()` 需要变体级 key，父 component set 无法被 import。因此 componentKey 必须存在于有 nodeId 的最小粒度对象上。  
**字段放置规则（4 种类型）**：  
- 类型 A：顶层 string nodeId → `"componentKey": null` 紧跟 nodeId 后  
- 类型 B：顶层 object nodeId → `"componentKey": {同键: null}` 紧跟 nodeId 后  
- 类型 C：variants/types 数组各项有 nodeId → 每项内加 `"componentKey": null`；顶层加占位 `"componentKey": null`（component set 标记）  
- 类型 D：variants/types 各项有 nodeId_default / nodeId_染色 → 分别加 `"componentKey_default": null` / `"componentKey_染色": null`  
- 例外：`slg_nameplate_gradient_overlay` 的 variants（`asset_type: css_gradient`，非 Figma 发布组件）不加 componentKey  
**值全部为 null**，后续由 ux-collect 补录。  
**影响范围**：`component-spec.json` 全体条目；`meta._note_componentKeys` 注释已同步更新。ux-collect/SKILL.md 补录步骤待 Phase 2 更新。

---

## §2 变更日志（新 session 必读）

> 格式：`日期 | 变更内容 | 涉及决策 | 执行状态`

| 日期 | 变更内容 | 涉及决策 | 执行状态 |
|---|---|---|---|
| 2026-05-15 | 全量清空 TGame 旧文件（8个旧 Skill + figma-design-spec/ 等遗留目录） | D1 | ✅ 已完成 |
| 2026-05-15 | 建立 decision-source/ 目录骨架 | D4 | ✅ 已完成 |
| 2026-05-15 | 写 AI-workflow-discussion-log.md（本文件，D1-D10 初始化） | D1-D10 | ✅ 已完成 |
| 2026-05-15 | 写 CLAUDE.md（XGame 新版，Skill 地图 + 路径注册） | D10 | ✅ 已完成 |
| 2026-05-15 | 写 ux-collect/SKILL.md | D5 | ✅ 已完成 |
| 2026-05-15 | 写 ia-generate/SKILL.md | D5, D6 | ✅ 已完成 |
| 2026-05-15 | 建 self-improving/ workflow-auditor/ unity-csharp-spec/ 骨架占位 | D7 | ✅ 已完成 |
| 2026-05-15 | 全部 SKILL.md 补加 YAML frontmatter（name/description/disable-model-invocation）+ 500行约束条款 | D11 | ✅ 已完成 |
| 2026-05-15 | ux-collect 新增 Design token 采集（tokens-decision.md + tokens-data.json）；ia-generate always-loaded 同步追加两文件 | D12 | ✅ 已完成 |
| 2026-05-15 | **ux-collect 首次真实执行**：采集 Figma「组件-模板」→「原子素材1 - TAB背景」（fileKey: jB3vJujGbA7pKX9rNIlJUt, node: 6897:17567）；读取 get_design_context + 13 张场景 get_screenshot；用户确认后写入 knowledge/common/component-decision.md（新建）+ component-spec.json（新建，26 个组件条目）。内容：Tab 背景按场景分 6 类 + 背景底板按场景分 8 类 + 命名规律速查；核心规则：select = 纹样不可拉伸，normal = 九宫格可拉伸。 | D4, D5 | ✅ 已完成 |
| 2026-05-15 | 修复 ux-collect bug：步骤3加"必须同时展示 MD+JSON 预览"；步骤4 `+` 改为 `且` 并加注"必须同时写入，不允许单独只写 MD"（layout/component 两对均适用） | D5 | ✅ 已完成 |
| 2026-05-15 | nodeId 架构落地：ux-collect 步骤1补采集 nodeId；ia-generate Component 清单加 nodeId 列；component-spec.json 全量补录 26 个组件 nodeId + meta 加 last_synced 字段 | D13 | ✅ 已完成 |
| 2026-05-15 | Phase 1 验证：发现 nodeId ≠ componentKey 问题；从源库批量采集 25 个 componentKey，写入 component-spec.json meta.componentKeys 查找表；验证 20 个可直接实例化，5 个需在 Copy 源文件中 Publish | D14 | ✅ 已完成 |
| 2026-05-15 | Phase 1 验证：确认 search_design_system 对 team library 不可检索（即使传 includeLibraryKeys 也返回空）；component-spec.json _note_componentKeys 写入禁用说明 | D15 | ✅ 已完成 |
| 2026-05-15 | ia-generate/SKILL.md：Component 清单表格加 componentKey 列；下游衔接章节去除 search-design-system 正面引用，加默认禁用注释（D14、D15） | D14, D15 | ✅ 已完成 |
| 2026-05-15 | ux-collect/SKILL.md：步骤1 search_design_system 加默认禁用警告；组件库采集展开为 nodeId+componentKey 双采集流程（use_figma on source lib → node.key）；nodeId 用途注追加 componentKey 用途说明（D14、D15） | D14, D15 | ✅ 已完成 |
| 2026-05-18 | component-spec.json 全体条目新增 componentKey 字段占位（null）：类型A顶层string nodeId旁、类型B顶层object nodeId旁、类型C variants/types每项内+顶层、类型D nodeId_default/nodeId_染色旁；meta._note_componentKeys 同步更新；废弃 meta.componentKeys 查找表设计 | D16 | ✅ 已完成 |
| 2026-05-18 | 双 Agent 唯一真实源重构：新增 `ai-shared/` 作为 canonical shared layer；`AGENTS.md` / `CLAUDE.md`、`.agents/skills/*`、`.claude/skills/*`、`.claude/commands/*` 改为入口壳；新增 `project-status.md` 与 `active-session.md`；`AI-workflow-discussion-log.md` 明确降级为历史档案与变更日志 | D10, D17 | ✅ 已完成 |
| 2026-05-18 | 删除废弃 command 资产 `figma-record`（共享正文 + Codex/Claude command shim），并将结构级变更归档流程改为“先对话审批，批准后写入 AI-workflow-discussion-log.md”；`state/` 继续即时更新 | D10, D17, D18 | ✅ 已批准并写入 |

---

## §3 Skill 地图快照

| Skill | Phase | 状态 | 职责简述 |
|---|---|---|---|
| ux-collect | 1 | ✅ SKILL.md 完成 | 从 Figma URL 采集决策源规则，写入 knowledge/ |
| ia-generate | 1 | ✅ SKILL.md 完成 | 读 knowledge/ + learnings/，推理产出 IA 结构化文档.md |
| self-improving | 2 | ⏳ 骨架占位 | 反馈 → bad case → 审批 → 蒸馏更新 knowledge/ |
| workflow-auditor | 3 | ⏳ 待 Phase 3 讨论 | 端到端验收审计（范围待定） |
| unity-csharp-spec | 3 | ⏳ 待 Phase 3 讨论 | C# 规范产出（范围待定） |

---

## §4 Phase 进度

### Phase 1 — 核心流验证（进行中）

- [x] 清空 TGame 旧文件
- [x] 建立 decision-source/ 目录结构
- [x] 写 AI-workflow-discussion-log.md（本文件）
- [x] 写 CLAUDE.md
- [x] 写 ux-collect/SKILL.md（含 frontmatter + 500行约束）
- [x] 写 ia-generate/SKILL.md（含 frontmatter + 500行约束）
- [x] 建 Phase 2/3 Skill 骨架目录（含 frontmatter + 500行约束）
- [ ] **验证**：输入真实策划需求 → 端到端跑链路 → 人工评估界面质量（评估点 1/2/3）

### Phase 2 — 学习闭环验证（未开始）

- [ ] 写 self-improving/SKILL.md
- [ ] **验证**：同一需求重跑，bad case 有明显减少

### Phase 3 — 配套工具（待讨论）

- [ ] 另开 Plan Mode 专题讨论 workflow-auditor 范围和设计
- [ ] 另开 Plan Mode 专题讨论 unity-csharp-spec 范围和设计

---

## §5 待讨论项

| # | 问题 | 备注 |
|---|---|---|
| Q1 | workflow-auditor Phase 3：验收维度如何定义？与 TGame 版本是否延续？ | 待单独 Plan Mode 讨论 |
| Q2 | unity-csharp-spec Phase 3：适用场景和输入格式？ | 待单独 Plan Mode 讨论 |
| Q3 | ~~knowledge/common/ 的初始内容：Phase 1 验证前，ux-collect 需要先采集哪个 Figma URL？~~ | ✅ 已解决（2026-05-15）：首次采集完成，写入 component-decision.md + component-spec.json |
| Q4 | ia-generate 的 specific/ 加载触发机制：何种语义关键词触发哪个 specific 文件？ | 在 ia-generate SKILL.md 中细化 |
---

## 补注 2026-05-18

### D17 - ux-collect 补强 componentKey 采集与写前校验

**背景**：本次在多组件 Figma 页面执行 `ux-collect` 时，`component-spec.json` 已录入 `nodeId`，但一批可实例化 variant 未自动录入 `componentKey`。复盘确认原因不是单次执行疏忽，而是 `ux-collect` 旧版流程只要求“读 Figma / 去重 / 给用户确认 / 写 knowledge”，没有把 `componentKey` 采集与校验写成强制步骤。  
**结论**：`componentKey` 是 `component-spec.json` 中可实例化组件的必填映射字段，不再视为事后补充信息。顶层规则组或分组容器允许 `componentKey = null`，但其所有可实例化 variant 必须补齐 `componentKey`。  
**执行结果**：已更新 `ai-shared/skills/ux-collect/SKILL.md`，新增以下硬约束：
- 读取 `componentKey` 时必须使用 `use_figma`，并先遵循 `figma-use` skill
- 实例节点记录 `mainComponent.key`
- Figma 真实组件节点记录自身 `componentKey`
- 规则组/分组容器允许顶层 `componentKey = null`
- 任何后续需要实例化的 variant 都必须补齐 `componentKey`
- 写入 `component-spec.json` 前必须校验 `nodeId + componentKey` 完整性，禁止出现“新增了 nodeId，但本应可实例化的 variant 仍缺 `componentKey`”的情况

### 变更日志补注

| 日期 | 变更内容 | 涉及决策 | 执行状态 |
|---|---|---|---|
| 2026-05-18 | 复盘并修正 ux-collect：补强 componentKey 采集与写前校验，明确实例用 `mainComponent.key`、真实组件用自身 `componentKey`、规则组顶层可为 null 但 variant 必须补齐；同步更新 workflow 日志 | D17 | ✅ 已完成 |

## 补注 2026-05-18（分子组件分层落地）

### D18 - 分子组件分层与实例化优先级显式化
**背景**：Phase 1 在继续巡检 `页签tab` 页面时确认，`tab_c_select_02`、`tab_c_normal`、`bg_c_boxblock_14/16` 等仅是原子层底板；而主 tab、局部 tab、聊天 tab、可展开 tab、联系人/黑名单条目、聊天操作浮窗、特殊语义按钮等，已经在 Figma 中以可复用组合组件存在。若下游仍默认从原子重新拼装，会丢失既有语义边界、状态封装与实例化入口。

**结论**：在 `decision-source/knowledge/common/component-spec.json` 中保留原有分类采集结果不变，同时新增并维护 `molecular_components` 作为唯一显式的分子层入口；后续实现侧若要选择可复用组件，应优先读取该区块，原子条目默认仅作为分子内部构件或兜底拼装材料。

**本轮确认的分子层条目（23项）**：
- 一级tab
- 二级tab
- 二级tab模块
- 聊天侧栏tab
- 聊天系统tab
- 竖向二级tab
- 背包主tab
- 背包装备tab
- 武将界面tab
- HUD详情tab
- 联系人
- 局部带图标tab
- 局部纯文字tab
- 聊天频道Tab
- 可展开tab
- 黑名单
- chat_action_popup
- btn_social_action
- btn_chat_control
- btn_cost_addon
- btn_context_special
- btn_jianzao
- btn_panel_side_collapse

**边界**：本轮为“索引增强”而非 schema 重构，不新增第二套分子专用 schema，不删除原有原子分类；`faction_color_systems`、箭头图标、编号图标、装饰纹样、纯视觉变体系统等，即使存在 variants，也不提升为 `layer: molecule`。

**影响**：`component-decision.md` 已同步写入“组件层级决策规则”与 “TAB 分子组件决策”；`project-status.md` 与 `active-session.md` 已同步记录该结构规则正式生效。`ia-generate` 后续应单开改造，优先消费 `molecular_components`，但该行为变更不属于本轮日志节点。

### 变更日志补注

| 日期 | 变更内容 | 涉及决策 | 执行状态 |
|---|---|---|---|
| 2026-05-18 | 在 `component-spec.json` 中固化 `molecular_components` 作为唯一显式分子层入口，并保留原分类作为原始采集归档与兜底检索 | D18 | 已完成人类批准后的正式落地 |
| 2026-05-18 | 在 `component-decision.md` 中明确“分子优先实例化，原子默认仅作内部构件或兜底材料”的总规则，并补充 TAB 分子组件适用边界 | D18 | 已完成 |
| 2026-05-18 | 将本轮结构性变更同步到 `project-status.md`、`active-session.md` 与 `AI-workflow-discussion-log.md`，作为共享知识源正式生效节点 | D18 | 已完成 |

## 补注 2026-05-18（ia-generate 分子优先消费）

### D19 - ia-generate 消费分子层优先级规则落地
**背景**：D18 只完成了知识库层的显式分层，如果 `ia-generate` 仍按原有习惯直接从原分类中找底板、图标和原子组件，就会继续绕过已确认的分子层入口，导致“知识库已分层，但生成行为未切换”的不一致。

**结论**：`ai-shared/skills/ia-generate/SKILL.md` 已补充正式消费顺序：组件选择时先检查 `component-spec.json -> molecular_components`，仅当没有可覆盖场景的分子组件时，才允许回退到原分类作为 atom fallback。若命中分子组件，输出中必须显式标注来源为 `molecular_components`；若回退到原子层，必须说明未使用分子组件的原因。

**影响**：自本节点起，`ia-generate` 的期望行为不再只是“能读 component-spec”，而是“按分子优先、原子兜底的规则产出组件清单”。这仍属于 Skill 规则层落地，不包含额外 schema 变更，也不代表已完成端到端实跑验证。

### 变更日志补注

| 日期 | 变更内容 | 涉及决策 | 执行状态 |
|---|---|---|---|
| 2026-05-18 | 在 `ai-shared/skills/ia-generate/SKILL.md` 中新增组件读取优先级，要求先读 `molecular_components`，原分类仅作 atom fallback | D19 | 已完成 |
| 2026-05-18 | 在 `ia-generate` 的 Component 决策规则中增加输出标注要求：分子命中必须标 `layer: molecule`，原子回退必须标 `layer: atom-fallback` | D19 | 已完成 |
| 2026-05-18 | 同步更新 `project-status.md` 与 `active-session.md`，移除“ia-generate 尚未消费分子层”的旧状态 | D19 | 已完成 |

## 补注 2026-05-18（仓库编码治理）

### D20 - 仓库文本编码统一为 UTF-8 with BOM，显示链路与落盘损坏分治
**背景**：本轮排查发现，多个共享 `.md` 文件在默认 `Get-Content` 路径下会显示乱码，但按显式 UTF-8 解码读取后内容正常。根因不是仓库内大面积错误转码，而是当前 Windows PowerShell 5.1 会话存在编码链路不一致：`chcp 936`、`[Console]::OutputEncoding = utf-8`、`[Console]::InputEncoding = gb2312`、`$OutputEncoding = us-ascii`。在这种前提下，如果不先区分“显示链路问题”和“文件已坏”，就会误把正常 UTF-8 文件当成需要修复的损坏文件。

**结论**：仓库目标文本类型统一采用 `UTF-8 with BOM + LF`。对编码问题采取分治策略：
- 可被严格 UTF-8 解码、仅在默认终端链路下乱码的文件，归类为显示链路问题，不重写内容
- 无法严格 UTF-8 解码、或严格解码后仍确认 mojibake 的文件，才归类为落盘损坏并进入内容修复
- 在方案 A 下，目标文本文件统一规范化为 UTF-8 with BOM，以降低 Windows 工具链误判为 GBK 的概率

**执行结果**：
- 新增 `.editorconfig`，为 `.md`、`.json`、`.txt`、`.yml`、`.yaml`、`.js`、`.ts`、`.html`、`.css` 约束 `utf-8`、`lf`
- 新增 `.gitattributes`，为同类文本文件声明 `text eol=lf working-tree-encoding=UTF-8`
- 新增 `ai-shared/docs/encoding-governance.md`，固化分类方法、修复边界和 PowerShell 读取规范
- 在 `ai-shared/docs/collaboration-protocol.md` 补充 Encoding Rules，明确“不要把默认终端乱码直接判定为文件损坏”
- 新增 `tools/encoding-audit.ps1`，作为只读审计入口，检查严格 UTF-8、BOM、疑似 mojibake 和处理建议
- 将 `decision-source/knowledge/common/component-spec.json` 与其余目标文本文件统一规范化为 UTF-8 with BOM
- 同步更新 `project-status.md` 与 `active-session.md`，将仓库编码治理结果纳入共享状态

**验证结论**：当前目标文本文件共 25 个，全部可被严格 UTF-8 解码，全部为 UTF-8 with BOM；本轮未发现明确需要内容修复的真实落盘 mojibake 文件。在当前 Windows PowerShell 5.1 环境下，默认 `Get-Content` 对典型中文文件已恢复正常显示。

### 变更日志补注

| 日期 | 变更内容 | 涉及决策 | 执行状态 |
|---|---|---|---|
| 2026-05-18 | 新增 `.editorconfig`、`.gitattributes`、`ai-shared/docs/encoding-governance.md`、`tools/encoding-audit.ps1`，建立仓库编码规范与只读审计入口 | D20 | 已完成 |
| 2026-05-18 | 在 `ai-shared/docs/collaboration-protocol.md` 增补 Encoding Rules，明确编码分类与读取规范 | D20 | 已完成 |
| 2026-05-18 | 将 `decision-source/knowledge/common/component-spec.json` 与其余目标文本文件统一规范化为 UTF-8 with BOM，并完成严格 UTF-8 复核 | D20 | 已完成 |
| 2026-05-18 | 完成全仓库目标文本类型编码复核：25 个文件全部严格 UTF-8、全部带 BOM，默认 `Get-Content` 对典型中文文件恢复正常显示 | D20 | 已完成 |
| 2026-05-18 | 将 BOM 策略与审计入口继续上收至 `project-workflow.md` 与 `path-registry.md`，明确后续新增文本文件必须遵循 UTF-8 with BOM + LF | D20 | 已完成 |
