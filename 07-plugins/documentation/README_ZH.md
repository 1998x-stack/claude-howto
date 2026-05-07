<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 文档插件

为您的项目提供全面的文档生成与维护能力。

## 功能特性

✅ 自动生成 API 文档  
✅ 创建与更新 README 文件  
✅ 文档与代码同步更新  
✅ 优化源代码注释  
✅ 生成实用代码示例  

## 安装方式

```bash
/plugin install documentation
```

## 包含内容

### 斜杠命令（Slash Commands）
- `/generate-api-docs` —— 生成 API 文档  
- `/generate-readme` —— 创建或更新 README  
- `/sync-docs` —— 将文档与代码变更同步  
- `/validate-docs` —— 验证文档完整性与准确性  

### 子智能体（Subagents）
- `api-documenter` —— 专注 API 文档生成的专家智能体  
- `code-commentator` —— 提升代码注释质量的智能体  
- `example-generator` —— 生成高质量代码示例的智能体  

### 文档模板（Templates）
- `api-endpoint.md` —— REST API 端点文档模板  
- `function-docs.md` —— 函数/方法级文档模板  
- `adr-template.md` —— 架构决策记录（ADR）模板  

### MCP 服务（MCP Servers）
- GitHub 集成：支持自动同步文档至 GitHub 仓库  

## 使用方法

### 生成 API 文档
```
/generate-api-docs
```

### 创建 README
```
/generate-readme
```

### 同步文档
```
/sync-docs
```

### 验证文档
```
/validate-docs
```

## 系统要求

- Claude Code 1.0 或更高版本  
- GitHub 访问权限（可选，仅用于文档同步功能）

## 示例工作流

```
用户：/generate-api-docs

Claude：
1. 扫描 `/src/api/` 目录下的全部 API 端点  
2. 调用 `api-documenter` 子智能体执行专项处理  
3. 提取函数签名及 JSDoc 注释  
4. 按模块/端点分类组织内容  
5. 套用 `api-endpoint.md` 模板进行格式化  
6. 生成结构清晰、内容详实的 Markdown 文档  
7. 内置 curl、JavaScript 和 Python 三种调用示例  

结果：
✅ API 文档已成功生成  
📄 新建文件如下：
   - docs/api/users.md  
   - docs/api/auth.md  
   - docs/api/products.md  
📊 覆盖率：23/23 个端点均已完整记录
```

## 模板使用说明

### API 端点模板  
适用于 REST API 端点的标准化文档编写，包含请求/响应示例、参数说明与错误码等完整信息。

### 函数文档模板  
适用于单个函数或方法的详细说明，涵盖参数、返回值、异常及使用场景。

### ADR 模板  
适用于记录关键架构决策（如技术选型、设计权衡），确保团队知识沉淀与可追溯性。

## 配置说明

如需启用 GitHub 文档同步，请配置 GitHub Token：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 最佳实践建议

- 文档应尽可能贴近对应代码（例如置于同一目录或使用内联注释）  
- 每次修改代码时同步更新相关文档  
- 文档中务必包含真实可用的实践示例  
- 定期运行 `/validate-docs` 进行一致性检查  
- 统一使用官方模板，保障风格与结构的一致性