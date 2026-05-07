--- BEGIN CONTENT ---
---
name: 配置 CI/CD 流水线
description: 实施预提交钩子（pre-commit hooks）和 GitHub Actions 以保障质量
tags: ci-cd, devops, 自动化
---

# 配置 CI/CD 流水线

根据项目类型，实施全面的 DevOps 质量门禁：

1. **分析项目**：识别编程语言、框架、构建系统及现有工具链  
2. **配置预提交钩子**，集成语言专属工具：
   - 格式化：Prettier / Black / gofmt / rustfmt 等  
   - 代码检查（Linting）：ESLint / Ruff / golangci-lint / Clippy 等  
   - 安全扫描：Bandit / gosec / cargo-audit / npm audit 等  
   - 类型检查：TypeScript / mypy / Flow（如适用）  
   - 测试：运行对应测试套件  
3. **创建 GitHub Actions 工作流**（位于 `.github/workflows/` 目录下）：
   - 在推送（push）或拉取请求（PR）时复现预提交检查  
   - 支持多版本/多平台矩阵（如适用）  
   - 构建与测试验证  
   - 部署步骤（如需）  
4. **验证流水线**：本地测试、创建测试 PR，确认所有检查均通过  

仅使用免费/开源工具；尊重项目已有配置；确保执行高效快速。

---
**最后更新时间**：2026 年 4 月 9 日

--- END CONTENT ---