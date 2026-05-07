---  
name: 设置 CI/CD 流水线  
description: 实现 pre-commit 钩子与 GitHub Actions，保障代码质量  
tags: ci-cd, devops, automation  
---  

# 设置 CI/CD 流水线  

构建面向项目的端到端 DevOps 质量门禁，具体实施步骤如下：

1. **项目分析**：识别所用编程语言、框架、构建系统及现有工具链  
2. **配置 pre-commit 钩子**（按语言选用对应工具）：  
   - 代码格式化：Prettier / Black / gofmt / rustfmt 等  
   - 代码检查（Linting）：ESLint / Ruff / golangci-lint / Clippy 等  
   - 安全扫描：Bandit / gosec / cargo-audit / npm audit 等  
   - 类型检查：TypeScript / mypy / Flow（如适用）  
   - 测试执行：运行对应测试套件  
3. **创建 GitHub Actions 工作流**（`.github/workflows/` 目录下）：  
   - 在 push / PR 触发时复现 pre-commit 检查  
   - 支持多版本/多平台矩阵（如适用）  
   - 构建与测试验证  
   - 部署步骤（按需添加）  
4. **流水线验证**：本地测试钩子、提交测试 PR、确认所有检查项通过  

优先使用免费/开源工具；尊重项目现有配置；确保各环节执行高效。  

---  
**最后更新**：2026 年 4 月 9 日