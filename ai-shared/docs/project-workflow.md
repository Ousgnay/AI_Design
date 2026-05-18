# XGame AI 设计工作流

> 核心定位：**信息生成，不是图像生成**  
> 流程链：业务逻辑 → 信息架构 IA → 信息实例化 → 自我学习  
> 当前状态：`ai-shared/state/project-status.md`  
> 轮换交接：`ai-shared/state/active-session.md`  
> 历史档案：`AI-workflow-discussion-log.md`

---

## Skill 地图

本项目使用以下 Skill（均位于 `ai-shared/skills/`）：

| Skill | Phase | 状态 | 职责 |
|---|---|---|---|
| **ux-collect** | 1 | ✅ 可用 | 从 Figma URL 采集 IA 决策源规则，写入 `decision-source/knowledge/` |
| **ia-generate** | 1 | ✅ 可用 | 读 knowledge/ + learnings/，推理产出 IA 结构化文档.md |
| **self-improving** | 2 | ⏳ 骨架占位 | 反馈 → bad case → 审批 → 蒸馏更新 knowledge/ |
| **workflow-auditor** | 3 | ⏳ 待讨论 | 端到端验收审计（范围待 Phase 3 讨论） |
| **unity-csharp-spec** | 3 | ⏳ 待讨论 | C# 规范产出（范围待 Phase 3 讨论） |

---

## 决策源路径

```text
[项目根]/decision-source/
├── knowledge/
│   ├── common/
│   └── specific/
└── learnings/
    ├── pending/
    └── approved/
```

---

## 核心数据流

```text
环节1  策划MD（必选）+ 竞品拆解MD（可选）
         ↓
环节2  /ia-generate
         读 knowledge/（only-read）+ learnings/（only-read）
         → 产出 IA 结构化文档.md
         ↓
       用户审阅 IA 文档，确认后手动触发 ↓
环节3  官方 Figma Skill 包（按需组合，不硬约束）
         figma-generate-design / figma-use / 其他相关 MCP
         → 产出 Figma 界面
         ↓
环节4  /self-improving（Phase 2）
         反馈 → bad case → learnings/pending
         → 人工审批 → 蒸馏进 knowledge → learnings 清除
```

`/ux-collect` 横切持续补充 `knowledge/`。

---

## 读取顺序

1. 先读 `ai-shared/state/project-status.md`
2. 再读 `ai-shared/state/active-session.md`
3. 需要项目来龙去脉时，再读 `AI-workflow-discussion-log.md`
4. 路径与权限问题统一看 `ai-shared/docs/path-registry.md`

---

## 结构级更新归档规则

- skill、共享协议、目录结构、入口壳等结构级更新，先在对话中生成待审变更草案
- 只有人类审批通过后，才写入 `AI-workflow-discussion-log.md`
- `ai-shared/state/project-status.md` 与 `ai-shared/state/active-session.md` 继续即时更新，不承载待审草案

---

## 文本编码约束

- 仓库文本文件默认使用 UTF-8 with BOM + LF。
- 适用范围：`.md`、`.json`、`.txt`、`.yml`、`.yaml`、`.js`、`.ts`、`.html`、`.css`。
- 新增或重写以上类型文件时，必须遵循 `.editorconfig` 与 `.gitattributes`，不要引入无 BOM 的同类文件。
- 进行编码排查时，先运行 `tools/encoding-audit.ps1`，不要仅凭默认终端显示结果判断文件是否损坏。
- 若发现默认显示异常但审计结果仍为严格 UTF-8，应优先按“显示链路问题”处理，而不是立即重写文件内容。
