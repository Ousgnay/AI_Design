---
name: self-improving
description: 接收人类反馈，归纳 bad case 写入 learnings/pending/，经人工审批后蒸馏更新 decision-source/knowledge/，实现越用越聪明。Phase 2 实现，当前为骨架占位。
disable-model-invocation: false
---

# self-improving

> **状态**：⏳ Phase 2 待实现（骨架占位）  
> **职责**：基于人类反馈归纳 bad case，经审批后蒸馏更新 `decision-source/knowledge/`，实现"越用越聪明"  
> **Phase**：2  
> **权限**：knowledge/ 读写；learnings/ 读写  
> **路径注册**：见 `ai-shared/docs/path-registry.md §跨 Skill 路径注册`

---

## 触发方式（Phase 2 实现后）

用户提供反馈文字或 Figma 批注截图，说"记录这个 bad case" 或 "/self-improving"。

---

## 职责概述

1. 接收人类反馈
2. AI 复盘归纳 bad case，对比现有 knowledge/，写入 `learnings/pending/`
3. 人工审批批准 → 移入 `learnings/approved/`
4. 蒸馏更新 `knowledge/` → 清除 `learnings/approved/`

---

## 约束

- **本文件行数约束**：SKILL.md 保持在 500 行以内。若需扩充内容导致超过 500 行，AI 必须先将新增内容以摘要形式呈现给用户审批，用户批准后方可写入。
