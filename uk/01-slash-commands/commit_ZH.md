--- BEGIN CONTENT ---
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 基于当前上下文创建 Git 提交
---

## 上下文

- 当前 Git 状态：!`git status`  
- 当前 Git 差异（相对于 HEAD）：!`git diff HEAD`  
- 当前分支：!`git branch --show-current`  
- 最近 10 条提交记录：!`git log --oneline -10`

## 你的任务

基于上述变更，创建一个 Git 提交。

- 若通过参数传入了提交消息，则直接使用该消息：`$ARGUMENTS`  
- 否则，请分析变更内容，并依据 [Conventional Commits](https://www.conventionalcommits.org/) 规范生成合适的提交消息：  
  - `feat:` 表示新增功能  
  - `fix:` 表示修复缺陷  
  - `docs:` 表示文档变更  
  - `refactor:` 表示代码重构  
  - `test:` 表示添加测试  
  - `chore:` 表示维护性任务  

---
**最后更新时间**：2026 年 4 月 9 日  
--- END CONTENT ---