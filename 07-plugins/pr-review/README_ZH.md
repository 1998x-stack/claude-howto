<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR 审查插件

端到端的 PR 审查工作流，涵盖安全、测试与文档检查。

## 功能特性

✅ 安全性分析  
✅ 测试覆盖率检查  
✅ 文档完整性验证  
✅ 代码质量评估  
✅ 性能影响分析  

## 安装方法

```bash
/plugin install pr-review
```

## 包含内容

### 斜杠命令（Slash Commands）
- `/review-pr` —— 全面的 PR 审查  
- `/check-security` —— 聚焦安全性的审查  
- `/check-tests` —— 测试覆盖率分析  

### 子智能体（Subagents）
- `security-reviewer` —— 安全漏洞检测  
- `test-checker` —— 测试覆盖率分析  
- `performance-analyzer` —— 性能影响评估  

### MCP 服务（MCP Servers）
- GitHub 集成，用于获取 PR 数据  

### 钩子（Hooks）
- `pre-review.js` —— 审查前校验逻辑  

## 使用方法

### 基础 PR 审查
```
/review-pr
```

### 仅执行安全检查
```
/check-security
```

### 仅检查测试覆盖率
```
/check-tests
```

## 系统要求

- Claude Code 1.0 或更高版本  
- GitHub 访问权限  
- Git 仓库环境  

## 配置说明

请配置您的 GitHub Token：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 示例工作流

```
用户：/review-pr

Claude：
1. 执行 pre-review 钩子（校验 Git 仓库有效性）  
2. 通过 GitHub MCP 获取 PR 相关数据  
3. 将安全性审查任务委派给子智能体 `security-reviewer`  
4. 将测试相关分析任务委派给子智能体 `test-checker`  
5. 将性能评估任务委派给子智能体 `performance-analyzer`  
6. 汇总所有子智能体的分析结果  
7. 生成并输出完整的审查报告  

输出结果：
✅ 安全性：未发现严重问题  
⚠️  测试：当前覆盖率 65%，建议提升至 80% 以上  
✅ 性能：无显著性能影响  
📝 建议：为边界场景补充测试用例
```