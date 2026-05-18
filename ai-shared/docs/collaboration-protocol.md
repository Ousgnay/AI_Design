# XGame 协作协议

> 目标：保证 Codex / Claude 在同一时间轴上轮换工作，但永远只有一个工具在写。  
> 当前状态看 `ai-shared/state/project-status.md`，交接看 `ai-shared/state/active-session.md`。

---

## Core Rule

同一时间轴只使用一款工具。

- 当前工具负责本轮修改
- 切换工具前必须完成交接
- 交接完成前，不启动下一工具写入

---

## Session Flow

1. 读取 `ai-shared/state/project-status.md`
2. 读取 `ai-shared/state/active-session.md`
3. 需要历史背景时，再读 `AI-workflow-discussion-log.md`
4. 当前工具完成本轮工作
5. 如有结构级变更，先在对话中提交待审变更草案
6. 人类批准后，才写入 `AI-workflow-discussion-log.md`
7. 更新 `ai-shared/state/project-status.md`
8. 更新 `ai-shared/state/active-session.md`，把 `handoff_ready` 设为 `true`
9. 下一工具只在读完 `project-status` + `active-session` 后继续

---

## Write Boundaries

- `AI-workflow-discussion-log.md`：只记录已批准的结构级历史变更，不做待审区，不做当前 TODO 板
- `ai-shared/state/project-status.md`：只写当前态，不展开长篇历史
- `ai-shared/state/active-session.md`：只写本轮交接信息

---

## Handoff Template

`active-session.md` 至少包含：

- `current_tool`
- `started_at`
- `scope`
- `files_in_play`
- `last_decisions`
- `next_step`
- `open_risks`
- `handoff_ready`

---

## Anti-Patterns

- 在两个工具里同时维护独立 TODO
- 未经审批就把结构级变更写入 `AI-workflow-discussion-log.md`
- 在历史档案里反复改写当前状态
- 在 skill 正文中写死工具私有路径
- 让一个工具未交接完就接着写
---

## Encoding Rules

- Repository text files use UTF-8 with BOM by default.
- Repository text files use LF line endings by default.
- The rule applies to `.md`, `.json`, `.txt`, `.yml`, `.yaml`, `.js`, `.ts`, `.html`, and `.css`.
- Do not treat default terminal garbling as proof that a file is damaged.
- When auditing or scripting in Windows PowerShell 5.1, read files explicitly as UTF-8 or verify bytes first.
- Before rewriting any file for encoding reasons, classify it as display-path issue, on-disk damage, or manual review using `ai-shared/docs/encoding-governance.md` and `tools/encoding-audit.ps1`.
