---
description: 清理代码、准备变更并创建 Pull Request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request 准备检查清单

在创建 PR 前，请执行以下步骤：

1. 运行代码格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 查看 Git 差异：`git diff HEAD`
4. 将变更添加到暂存区：`git add .`
5. 按照 Conventional Commits 规范撰写提交信息：
   - `fix:` 修复错误
   - `feat:` 新增功能
   - `docs:` 文档更新
   - `refactor:` 代码重构
   - `test:` 添加测试
   - `chore:` 维护性任务

6. 生成 PR 描述，内容需包含：
   - 变更内容
   - 变更原因
   - 已执行的测试
   - 潜在影响

---
**最后更新**：2026 年 4 月 9 日