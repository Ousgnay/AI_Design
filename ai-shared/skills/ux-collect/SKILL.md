---
name: ux-collect
description: 从 Figma URL 采集 IA 决策源规则（含 design system tokens 与 responsive 规则），写入 decision-source/knowledge/。触发条件：用户提供 Figma URL 并要求采集。
disable-model-invocation: false
---

# ux-collect

> **职责**：从 Figma URL 采集 IA 决策源资料，写入 `decision-source/knowledge/`
> **Phase**：1
> **权限**：knowledge/ 读写；learnings/ 无权限
> **路径注册**：见 `ai-shared/docs/path-registry.md` 中的 Skill 路径注册；禁止在本文件内硬编码路径

---

## 触发方式

用户提供 Figma URL，然后说“采集这个 Figma”或“/ux-collect”。

---

## 执行流程

### 步骤 1 — 读取 Figma 内容

使用官方 Figma MCP 工具读取用户提供的 URL：
- `get_design_context`
- `get_metadata`
- `search_design_system`
- `get_screenshot`

如果本次采集会写入 `component-spec.json` 这类组件数据文件，必须把组件的 `nodeId` 与 `componentKey` 一并采集：
- 优先记录 Figma 组件节点自身的 `componentKey`
- 若当前节点是实例，记录 `mainComponent.key`
- 若是 AI 为知识库归纳出来的“变体组/规则组”而不是 Figma 中真实存在的单节点，允许顶层 `componentKey = null`
- 但凡某个 variant 后续需要被实例化，就必须补齐该 variant 的 `componentKey`
- 需要读取 `componentKey` 时，必须调用 `use_figma`，并先遵循 `figma-use` skill；不能只依赖 `get_design_context` / `get_metadata`

如果本次采集会写入 `component-spec.json`，还必须先判断组件层级归属：
- 若目标是完整业务块、完整状态栏、完整信息模块、地图对象标识模块等高阶复合单元，优先写入 `organism_components`
- 若目标是语义完整、状态完整的复合交互单元，但还未达到完整业务块层级，写入 `molecular_components`
- 若目标仅是底板、图标、纹样、切图、标签底图或其他底层构件，保留在原分类区块或 `atomic_component_sets`
- 不得因为画板上摆在一起，就把多个分子/原子误记成组织层；只有当 Figma 中已存在明确组织层组件入口，或经规则归纳确认其承载完整业务块语义时，才提升为 `organism_components`

### 步骤 2 — 先读现有 knowledge/ 避免重复

读取 `decision-source/knowledge/common/` 下已有文件，判断是否重复。

同时必须先判断本次采集内容属于哪一类知识文件：

- `tokens`
  - 数据写入 `tokens-data.json`
  - 规则写入 `tokens-decision.md`
- `component`
  - 数据写入 `component-spec.json`
  - 规则写入 `component-decision.md`
- `layout`
  - 数据写入 `layout-spec.json`
  - 规则写入 `layout-decision.md`
- `responsive`
  - 数据写入 `responsive-spec.json`
  - 规则写入 `responsive-decision.md`
- `flow`
  - 规则默认写入 `flow-decision.md`

判定原则：

- 若采集对象是颜色、字号、样式、effect、变量等设计 token，归为 `tokens`
- 若采集对象是可实例化组件、组件层级、变体与实例化规则，归为 `component`
- 若采集对象是页面骨架、分区方式、界面分类、容器结构与布局范式，归为 `layout`
- 若采集对象是安全区、屏幕比例、元素挂靠逻辑、位置/尺寸适配策略、背景/列表/tips/弹窗的多分辨率适配规则，归为 `responsive`
- 若采集对象是页面之间的关系、入口跳转、交互链路、状态流转、步骤顺序与前后置依赖，归为 `flow`

### 步骤 3 — 与用户协作提炼规则

AI 整理初步采集内容后，必须先呈现给用户。

若本次采集属于 layout 家族页、模板页或规范页，还必须先完成以下解释动作，再给用户确认：
- 若页面右侧存在成列文字说明、问题记录、标注说明，默认按与左侧示例的横向位置和 `y` 轴邻近关系进行映射，不得把右侧说明误记为独立 layout
- 若一个页面同时包含“空白模板 + 多个具体变体”，应先抽取空白模板的共性骨架，再抽取各变体的差异结构
- 若对象同时具备 layout template 与真实 component 双重属性，必须先向用户说明会并行写入 `layout-*` 与 `component-*`
- 若页面是满屏结果层、全屏浮窗、主界面覆盖层等特殊界面，应默认按 `layout-first` 方式解释整页结构，只把其中真实存在的子级 `COMPONENT` / `COMPONENT_SET` 单独归入 `component-*`

若本次采集属于 responsive 规范页、适配规范页或图片化规则页，还必须先完成以下解释动作，再给用户确认：
- 若页面内容量很大，必须按用户指定或按自然分页分批读取，避免一次性读取整页导致上下文爆量
- 若页面包含大量 image、比例框、裁切对比图或截图示意，必须先做语义归纳，再抽象成“可复用规则”；不得把示意图本身误记为 layout template
- 若当前规范页没有稳定的结构化 frame 可记录 `responsive-spec.json` 的区块数据，允许先只写 `responsive-decision.md` 为权威规则，并在 `responsive-spec.json` 中保留来源页与“待后续结构化”的占位元数据
- 若同一规则在多个示意图中重复出现，应提炼为单条通用规则，并补充适用范围与例外条件，而不是逐图重复抄写

### 步骤 4 — 写入 knowledge/

用户批准后，将规则写入对应目录和文件。

如果本次写入包含 `component-spec.json`，写入前必须完成以下校验：
- 每个新增组件条目都要有 `nodeId`
- 每个可实例化组件或 variant 都要有 `componentKey`
- 只有“归纳出来的分组条目”允许顶层 `componentKey = null`
- 不允许出现“新增了 nodeId，但本应可实例化的 variant 仍缺 `componentKey`”的情况
- 若来源是 `component_set` 家族，不能只记录顶层 set；所有后续可能被真实实例化的 variant，都要单独补齐自己的 `componentKey`

如果本次写入包含 `layout-spec.json`，写入前必须完成以下校验：
- 每个 layout 条目都要有稳定的 `name`
- 每个 layout 条目都要有明确的 `category`
- 若 layout 来自真实 Figma 页面，还应记录来源 page 或 node 信息
- layout 来源可以是 `frame`、`component`、`component_set` 或其他稳定表达整页骨架的节点，不要求一定是可实例化组件
- 若用户提供了额外语义提示，应一并记录为 layout 命名、分类与使用场景判断依据
- layout 需要记录整页主要 UI 区块的结构化数据，包括位置、尺寸、对齐与适配信息
- `layout-spec.json` 只存结构化 layout 数据，不混入长篇规则说明
- 若来源是弹窗家族、模板家族或 `component_set` 家族，应优先录入空白模板或共性骨架，再录入具体变体
- 若 layout 与 component 同源共存，layout 侧记录家族骨架和变体结构，component 侧记录真实可实例化入口与 `componentKey`
- 若页面为满屏覆盖层、结果层或主界面叠加层，不得因视觉完整就把整页 frame 误记为普通组件；应以 layout 为主，仅拆出真实发布组件

如果本次写入包含 `responsive-spec.json`，写入前必须完成以下校验：
- `responsive-decision.md` 必须作为本次 responsive 采集的权威规则文件
- `responsive-spec.json` 至少要记录来源 file/page/node、采集状态、当前是否具备结构化模板、以及后续是否需要补 region 级数据
- 若当前来源只是规范说明页、对比图或图片化案例，而非稳定模板，不得伪造 `regions`、`anchors` 或整页结构化坐标
- 若已经可以抽象出稳定适配类别，可在 `responsive-spec.json` 中记录类别骨架、设备比例范围、规则覆盖面等轻结构化信息
- 若用户明确说明“当前先只要通用规则”，应优先保证 `responsive-decision.md` 的可读性和可复用性，不为凑结构强行补 spec 细节

---

## 约束

- **不得**写入 learnings/ 目录
- **不得**修改 ia-generate 的产出文件
- **不得**在本文件内硬编码 `decision-source/` 路径
- 每次采集必须经过用户确认后才写入
- 对 `component-spec.json` 的新增或补录，`componentKey` 视为必填字段，除非该条目明确是知识库分组容器而非真实 Figma 组件
- **本文件行数约束**：SKILL.md 保持在 500 行以内。若需扩充内容导致超过 500 行，AI 必须先将新增内容以摘要形式呈现给用户审批，用户批准后方可写入。
