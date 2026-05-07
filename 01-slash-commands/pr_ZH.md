--- BEGIN CONTENT ---
---
description: 清理代码、暂存变更并准备拉取请求（Pull Request）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# 拉取请求（PR）准备清单

创建 PR 前，请依次执行以下步骤：

1. 运行代码格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 查看变更差异：`git diff HEAD`
4. 暂存所有变更：`git add .`
5. 按约定式提交（Conventional Commits）规范编写提交信息：
   - `fix:` 修复缺陷
   - `feat:` 新增功能
   - `docs:` 文档更新
   - `refactor:` 代码重构
   - `test:` 添加测试
   - `chore:` 维护性任务

6. 生成 PR 摘要，需包含以下内容：
   - 修改了什么
   - 为何修改
   - 已执行的测试
   - 潜在影响

---
**最后更新时间**：2026 年 4 月 9 日

--- END CONTENT ---