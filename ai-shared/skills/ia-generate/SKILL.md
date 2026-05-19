---
name: ia-generate
description: 读取 decision-source/knowledge/ + learnings/，结合策划 MD 推理产出 IA 结构化文档。决策层：流程 / 容器 / 布局 / 状态 / Component。触发条件：用户提供策划文档并要求“生成 IA”或“/ia-generate”。
disable-model-invocation: false
---

# ia-generate

> **职责**：读取决策源 + 业务逻辑输入，推理产出 IA 结构化文档
> **Phase**：1
> **权限**：knowledge/ 只读，learnings/ 只读；不得写入任何共享知识文件
> **路径注册**：见 `ai-shared/docs/path-registry.md`

---

## 触发方式

用户输入策划文档（MD 格式），并要求“生成 IA”或“/ia-generate”。

---

## 输入

| 输入 | 必填 | 说明 |
|---|---|---|
| 策划结构化文档 `.md` | 必填 | 功能 / 系统业务逻辑说明 |
| 竞品拆解 `.md` | 可选 | 竞品分析参考，用于补充决策依据 |

---

## 决策源读取规则

### 固定读取（always-loaded）

每次执行必读：
- `decision-source/knowledge/common/flow-decision.md` - 流程推理案例
- `decision-source/knowledge/common/layout-decision.md` - 容器选择 + 布局规则
- `decision-source/knowledge/common/layout-spec.json` - 布局模板数据
- `decision-source/knowledge/common/responsive-decision.md` - 通用适配规则
- `decision-source/knowledge/common/responsive-spec.json` - 适配规则元数据 / 结构化骨架
- `decision-source/knowledge/common/component-decision.md` - 组件使用规范
- `decision-source/knowledge/common/component-spec.json` - 组件数据
- `decision-source/knowledge/common/tokens-decision.md` - Design token 使用规范
- `decision-source/knowledge/common/tokens-data.json` - Design token 原始数据

如果上述文件不存在，继续执行，但必须在 IA 文档中标注“决策源为空，以下判断基于通用 SLG 设计原则”。

### 组件读取优先级（component resolution order）

读取 `component-spec.json` 时，组件选择必须遵循以下优先级：
- 先检查 `organism_components`，判断是否已存在语义完整、结构完整、可直接承载一个业务块的组织层组件。
- 先检查 `molecular_components`，判断是否已存在语义完整、状态完整、可直接复用的分子组件。
- 只有当 `organism_components` 与 `molecular_components` 中都不存在可覆盖当前场景的条目时，才回退到原分类中的原子 / 底板 / 图标组件。
- 原分类条目默认视为“原始采集归档 + 底层构件检索池”，不是优先实例化入口。
- 若同一语义同时存在组织层、分子与原子方案，必须优先输出组织层；若无组织层再输出分子方案，并在组件清单中说明低层方案未采用。

### 按需读取（semantic-loaded）

根据策划文档中的语义关键词，按需读取 `decision-source/knowledge/specific/` 下相关文件。每个 specific 文件的 frontmatter 中有 `loaded_when` 字段，匹配即加载。

### 参考读取（approved learnings）

读取 `decision-source/learnings/approved/` 下的已批准 bad case，作为负例参考。

---

## 执行流程

### 步骤 1 - 理解业务逻辑

通读策划文档，提取：
- 核心功能目标
- 用户操作流程
- 数据实体
- 状态树
- 入口与出口

### 步骤 2 - 逐层推理 IA

按以下 5 个决策层依次推理：

**决策层 1 - 流程推理**  
基于业务逻辑，画出用户操作流程图（文字版）。

**决策层 2 - 界面容器选择**  
为每个流程节点选择合适的界面容器。

**决策层 3 - 单界面布局区划**  
对每个容器划分信息层级和布局区域。

**决策层 4 - 界面级状态树**  
列出每个界面的所有状态。

**决策层 5 - Component 决策**  
对每个信息单元决定使用的组件。

> **Component 准确性是 Phase 1 的核心评估点。必须明确列出每个组件的引用来源。**

### Component 决策附加规则

- 若目标是完整业务块、完整状态栏、完整信息模块、地图对象标识模块等高阶复合单元，先匹配 `organism_components`。
- 若命中组织层组件，输出时应直接引用该组织层组件名称、`nodeId`、`componentKey`，并标注来源为 `component-spec.json -> organism_components`。
- 若目标是完整 tab、条目、弹出操作菜单、带业务语义按钮、聊天控制区等复合交互单元，先匹配 `molecular_components`。
- 若命中分子组件，输出时应直接引用该分子组件名称、`nodeId`、`componentKey`，并标注来源为 `component-spec.json -> molecular_components`。
- 只有在知识库中找不到可复用组织层与分子层，或策划明确要求新组合时，才允许退回原子层拼装；此时必须在“决策备注”中说明为什么没有使用更高层组件。
- 不得因为原子层视觉更接近，就绕过已存在的组织层或分子组件；语义完整性优先于外观相似度。
- 对以下典型场景，默认先查分子层：主 tab、局部 tab、聊天 tab、可展开 tab、联系人 / 黑名单条目、聊天操作浮窗、特殊语义按钮。
- 对以下典型场景，默认先查组织层：完整信息卡、完整状态栏、地图对象标记、带多分子组合的业务模块。

### 步骤 3 - 产出 IA 结构化文档

生成 IA 文档（`.md` 格式），保存到用户指定位置；若用户未指定，默认放在项目根目录下的命名文件中。

---

## 输出格式

```markdown
# [界面/功能名] - IA 结构化文档
...
```

---

## 约束

- 不得写入 knowledge/ 或 learnings/ 中的任何文件
- 不得修改策划文档原文
- 不得在本文件内硬编码 `decision-source/` 路径
- Component 清单中每一项都必须明确标注来源
- 若组件来自 `organism_components`，必须显式标注 `layer: organism`
- 若组件来自 `molecular_components`，必须显式标注 `layer: molecule`
- 若组件来自原分类兜底拼装，必须显式标注 `layer: atom-fallback`
- 软约束偏离时必须在“决策备注”中说明理由
- `SKILL.md` 需保持在 500 行以内；若后续扩展超过 500 行，必须先摘要给用户审批后再写入

---

## 下游衔接

IA 文档产出后，工作流进入下一环节：
1. 用户审阅 IA 文档，确认或修改。
2. 用户手动触发官方 Figma Skill 包。
3. `search_design_system` 默认不用于本项目组件发现；组件应通过 `component-spec.json` 中的 `componentKey` 实例化。
4. 若出现 bad case，由用户记录，待 Phase 2 接入 `/self-improving`。
