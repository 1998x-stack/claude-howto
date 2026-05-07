<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps 自动化插件

面向部署、监控与事件响应的端到端 DevOps 自动化解决方案。

## 功能特性

✅ 自动化部署  
✅ 回滚流程  
✅ 系统状态监控  
✅ 事件响应工作流  
✅ 与 Kubernetes 深度集成  

## 安装方法

```bash
/plugin install devops-automation
```

## 插件内容概览

### 斜杠命令（Slash Commands）
- `/deploy` — 部署至生产环境或预发布环境（staging）  
- `/rollback` — 回滚至上一版本  
- `/status` — 检查系统当前运行状态  
- `/incident` — 处理生产环境突发事件  

### 子智能体（Sub-agents）
- `deployment-specialist` — 专注执行部署任务  
- `incident-commander` — 统筹协调事件响应流程  
- `alert-analyzer` — 实时分析系统健康状况与告警  

### MCP 服务器（MCP Servers）
- Kubernetes 集成服务  

### 脚本（Scripts）
- `deploy.sh` — 部署自动化脚本  
- `rollback.sh` — 回滚自动化脚本  
- `health-check.sh` — 系统健康检查工具  

### 钩子（Hooks）
- `pre-deploy.js` — 部署前校验（如 kubectl 可用性、集群连接性）  
- `post-deploy.js` — 部署后任务（如等待 Pod 就绪、执行冒烟测试）  

## 使用示例

### 部署至预发布环境（Staging）
```
/deploy staging
```

### 部署至生产环境（Production）
```
/deploy production
```

### 执行回滚操作
```
/rollback production
```

### 查询系统状态
```
/status
```

### 启动事件处理流程
```
/incident
```

## 系统要求

- Claude Code 1.0 或更高版本  
- 已安装 Kubernetes 命令行工具（kubectl）  
- 已配置对目标 Kubernetes 集群的访问权限  

## 配置说明

请确保正确设置 Kubernetes 配置文件路径：
```bash
export KUBECONFIG=~/.kube/config
```

## 典型工作流示例

```
用户：/deploy production

Claude：
1. 触发 pre-deploy 钩子（校验 kubectl 是否可用、验证集群连接）  
2. 将任务委派给子智能体 `deployment-specialist`  
3. 执行 `deploy.sh` 脚本  
4. 通过 Kubernetes MCP 服务实时监控部署进度  
5. 触发 post-deploy 钩子（等待所有 Pod 进入就绪状态、运行冒烟测试）  
6. 返回完整部署结果摘要  

执行结果：
✅ 部署成功完成  
📦 版本号：v2.1.0  
🚀 Pod 状态：3/3 已就绪  
⏱️  总耗时：2 分 34 秒
```