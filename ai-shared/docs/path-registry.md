# XGame 路径注册

> 唯一职责：集中管理共享路径、权限边界和工具入口壳的指向关系。  
> canonical skill/command 正文只引用这里，不再硬编码 `.claude/`、`.agents/`、`AGENTS.md` 或 `CLAUDE.md`。

---

## Canonical Shared Roots

```text
ai-shared/
├── docs/
│   ├── project-workflow.md
│   ├── path-registry.md
│   ├── collaboration-protocol.md
│   └── encoding-governance.md
├── state/
│   ├── project-status.md
│   └── active-session.md
├── skills/
│   ├── ia-generate/SKILL.md
│   ├── ux-collect/SKILL.md
│   ├── self-improving/SKILL.md
│   ├── workflow-auditor/SKILL.md
│   └── unity-csharp-spec/SKILL.md
└── commands/
```

---

## Tool Entry Shims

| 入口 | 角色 |
|---|---|
| `AGENTS.md` | Codex 入口壳 |
| `CLAUDE.md` | Claude 入口壳 |
| `.agents/skills/*/SKILL.md` | Codex 兼容入口壳 |
| `.claude/skills/*/SKILL.md` | Claude 兼容入口壳 |

入口壳只做两件事：
- 告诉工具去读 `ai-shared/`
- 不承载可编辑正文

---

## 跨 Skill 路径注册

| Skill | 读取路径 | 写入路径 |
|---|---|---|
| `ux-collect` | `decision-source/knowledge/`（读现有规则，避免重复） | `decision-source/knowledge/common/` 或 `specific/` |
| `ia-generate` | `decision-source/knowledge/common/*`<br>`decision-source/knowledge/specific/*`<br>`decision-source/learnings/approved/*` | 无 |
| `self-improving` | `decision-source/knowledge/*`<br>`decision-source/learnings/*` | `decision-source/learnings/pending/`<br>`decision-source/knowledge/` |
| `workflow-auditor` | Phase 3 再定 | Phase 3 再定 |
| `unity-csharp-spec` | Phase 3 再定 | 无 |

---

## 权限矩阵

| Skill | knowledge/ | learnings/ |
|---|---|---|
| `ux-collect` | 读写 | 无权限 |
| `ia-generate` | 只读 | 只读 |
| `self-improving` | 读写 | 读写 |
| `workflow-auditor` | Phase 3 再定 | Phase 3 再定 |
| `unity-csharp-spec` | Phase 3 再定 | 无 |

---

## Shared State

| 文件 | 作用 |
|---|---|
| `ai-shared/state/project-status.md` | 当前项目状态唯一真实源 |
| `ai-shared/state/active-session.md` | 当前会话交接唯一真实源 |
| `AI-workflow-discussion-log.md` | 历史档案与变更日志，只追加 |

## Encoding Governance

| 文件 | 作用 |
|---|---|
| `ai-shared/docs/encoding-governance.md` | 仓库文本编码策略、分类规则、修复边界 |
| `.editorconfig` | 新增/编辑文本文件时的编码与换行默认值 |
| `.gitattributes` | Git 文本归类与换行约束 |
| `tools/encoding-audit.ps1` | 只读编码巡检入口 |

---

## Private Boundary

以下内容保留为工具私有，不进入共享真实源：

- `.claude/settings.local.json`
- `.claude/scheduled_tasks.lock`
- `.claude/.obsidian/`
- 本地缓存、日志、会话临时文件

---

## Rules

- canonical skill/command 正文只能引用 `ai-shared/docs/path-registry.md`
- skill 内部不得再硬编码工具特有路径
- 结构级更新完成后，先在对话中提交待审变更草案；只有人类批准后，才可写入 `AI-workflow-discussion-log.md`
- 当前状态写 `project-status.md`
- 交接状态写 `active-session.md`
- 历史决策与变更日志写 `AI-workflow-discussion-log.md`
