<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 文档插件（Documentation Plugin）

为您的项目提供全面的文档生成与维护能力。

## 功能特性

✅ 自动生成 API 文档  
✅ 创建与更新 README 文件  
✅ 同步代码变更至文档  
✅ 优化源代码注释  
✅ 生成实用代码示例  

## 安装方法

```bash
/plugin install documentation
```

## 插件内容概览

### 斜杠命令（Slash Commands）
- `/generate-api-docs` — 生成 API 文档  
- `/generate-readme` — 创建或更新 README 文件  
- `/sync-docs` — 将文档与代码变更同步  
- `/validate-docs` — 验证文档完整性与准确性  

### 子智能体（Sub-agents）
- `api-documenter` — 专注 API 文档的专业子智能体  
- `code-commentator` — 提升代码注释质量的子智能体  
- `example-generator` — 生成多语言代码示例的子智能体  

### 文档模板（Templates）
- `api-endpoint.md` — API 端点标准文档模板  
- `function-docs.md` — 函数/方法级文档模板  
- `adr-template.md` — 架构决策记录（Architecture Decision Record, ADR）模板  

### MCP 服务器（MCP Servers）
- GitHub 集成：支持自动同步文档至 GitHub 仓库  

## 使用方式

### 生成 API 文档
```
/generate-api-docs
```

### 创建 README 文件
```
/generate-readme
```

### 同步文档内容
```
/sync-docs
```

### 验证文档质量
```
/validate-docs
```

## 系统要求

- Claude Code 1.0 或更高版本  
- GitHub 访问权限（可选，仅用于同步功能）  

## 典型工作流示例

```
用户：/generate-api-docs

Claude：
1. 扫描 `/src/api/` 目录下的全部 API 端点  
2. 将任务委派给子智能体 `api-documenter`  
3. 提取函数签名及 JSDoc 注释  
4. 按模块/端点结构化组织内容  
5. 应用 `api-endpoint.md` 模板  
6. 生成结构清晰、格式规范的 Markdown 文档  
7. 内置多种调用示例：curl、JavaScript 与 Python  

执行结果：
✅ API 文档已成功生成  
📄 新建文件如下：
   - docs/api/users.md  
   - docs/api/auth.md  
   - docs/api/products.md  
📊 覆盖率：23 个端点全部完成文档化  
```

## 模板使用说明

### API 端点模板  
适用于 RESTful API 端点的完整文档编写，包含请求/响应示例、参数说明与状态码详解。

### 函数文档模板  
适用于单个函数或方法的详细说明，涵盖输入输出、异常处理与使用场景。

### ADR 模板  
用于系统性地记录关键架构决策，包括背景、选项分析、最终选择及影响评估。

## 配置说明

如需启用 GitHub 文档同步，请配置 GitHub Token：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 最佳实践建议

- 将文档紧邻对应代码存放（如放在同一目录或相邻目录）  
- 每次修改代码时同步更新相关文档  
- 文档中务必包含真实、可运行的代码示例  
- 定期执行 `/validate-docs` 进行一致性检查  
- 始终使用统一模板，确保团队文档风格一致