--- BEGIN CONTENT ---
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [提交信息]
description: 基于上下文创建 Git 提交
---

## 上下文

- 当前 Git 状态：!`git status`  
- 当前 Git 差异：!`git diff HEAD`  
- 当前分支：!`git branch --show-current`  
- 最近提交记录：!`git log --oneline -10`

## 你的任务

根据上述变更，执行一次 Git 提交。

若通过参数提供了提交信息，则直接使用：$ARGUMENTS  

否则，请分析变更内容，并按约定式提交（Conventional Commits）格式生成合适的提交信息：  
- `feat:` 表示新增功能  
- `fix:` 表示修复 Bug  
- `docs:` 表示文档变更  
- `refactor:` 表示代码重构  
- `test:` 表示添加测试  
- `chore:` 表示维护性任务  

---
**最后更新时间**：2026 年 4 月 9 日  
--- END CONTENT ---