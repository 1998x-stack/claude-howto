<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR 审查插件

端到端的 Pull Request（PR）审查工作流，涵盖安全检查、测试覆盖分析与文档验证。

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
- `/review-pr` — 执行全面的 PR 审查  
- `/check-security` — 聚焦安全性的专项审查  
- `/check-tests` — 测试覆盖率分析  

### 子智能体（Sub-agents）
- `security-reviewer` — 检测安全漏洞  
- `test-checker` — 分析测试覆盖率  
- `performance-analyzer` — 评估对性能的影响  

### MCP 服务器（MCP Servers）
- 与 GitHub 集成，获取 PR 相关数据  

### 钩子（Hooks）
- `pre-review.js` — PR 审查前的预校验逻辑  

## 使用方式

### 基础 PR 审查
```
/review-pr
```

### 仅执行安全性检查
```
/check-security
```

### 仅检查测试覆盖率
```
/check-tests
```

## 系统要求

- Claude Code 1.0 或更高版本  
- 具备 GitHub 访问权限  
- 已配置本地 Git 仓库  

## 配置说明

请设置 GitHub 个人访问令牌（Token）：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 示例工作流

```
用户：/review-pr

Claude：
1. 触发 pre-review 钩子（校验 Git 仓库状态）  
2. 通过 GitHub MCP 接口获取 PR 数据  
3. 将安全性审查任务委派给子智能体 `security-reviewer`  
4. 将测试相关分析委派给子智能体 `test-checker`  
5. 将性能影响评估委派给子智能体 `performance-analyzer`  
6. 汇总所有子智能体的发现结果  
7. 生成结构清晰、可操作的综合审查报告  

审查结果：
✅ 安全性：未发现高危或严重安全问题  
⚠️ 测试覆盖：当前覆盖率 65%，建议提升至 80% 以上  
✅ 性能：无显著性能退化  
📝 建议：补充边界条件相关的单元测试用例
```