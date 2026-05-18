---
name: ux-collect
description: 从 Figma URL 采集 IA 决策源规则（含 design system tokens），写入 decision-source/knowledge/。触发条件：用户提供 Figma URL 并要求采集。
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

### 步骤 2 — 先读现有 knowledge/ 避免重复

读取 `decision-source/knowledge/common/` 下已有文件，判断是否重复。

### 步骤 3 — 与用户协作提炼规则

AI 整理初步采集内容后，必须先呈现给用户。

### 步骤 4 — 写入 knowledge/

用户批准后，将规则写入对应目录和文件。

如果本次写入包含 `component-spec.json`，写入前必须完成以下校验：
- 每个新增组件条目都要有 `nodeId`
- 每个可实例化组件或 variant 都要有 `componentKey`
- 只有“归纳出来的分组条目”允许顶层 `componentKey = null`
- 不允许出现“新增了 nodeId，但本应可实例化的 variant 仍缺 `componentKey`”的情况

---

## 约束

- **不得**写入 learnings/ 目录
- **不得**修改 ia-generate 的产出文件
- **不得**在本文件内硬编码 `decision-source/` 路径
- 每次采集必须经过用户确认后才写入
- 对 `component-spec.json` 的新增或补录，`componentKey` 视为必填字段，除非该条目明确是知识库分组容器而非真实 Figma 组件
- **本文件行数约束**：SKILL.md 保持在 500 行以内。若需扩充内容导致超过 500 行，AI 必须先将新增内容以摘要形式呈现给用户审批，用户批准后方可写入。
