<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps 自动化插件

面向部署、监控与事件响应的完整 DevOps 自动化解决方案。

## 功能特性

✅ 自动化部署  
✅ 回滚流程  
✅ 系统健康监控  
✅ 事件响应工作流  
✅ Kubernetes 集成  

## 安装方法

```bash
/plugin install devops-automation
```

## 包含内容

### 斜杠命令（Slash Commands）
- `/deploy` —— 部署至生产环境或预发布环境  
- `/rollback` —— 回滚至上一版本  
- `/status` —— 检查系统健康状态  
- `/incident` —— 处理生产环境事件  

### 子智能体（Subagents）
- `deployment-specialist` —— 专注部署操作  
- `incident-commander` —— 协调事件响应  
- `alert-analyzer` —— 分析系统健康告警  

### MCP 服务（MCP Servers）
- Kubernetes 集成  

### 脚本（Scripts）
- `deploy.sh` —— 部署自动化脚本  
- `rollback.sh` —— 回滚自动化脚本  
- `health-check.sh` —— 健康检查工具脚本  

### 钩子（Hooks）
- `pre-deploy.js` —— 部署前校验  
- `post-deploy.js` —— 部署后任务  

## 使用方法

### 部署至预发布环境
```
/deploy staging
```

### 部署至生产环境
```
/deploy production
```

### 执行回滚
```
/rollback production
```

### 查看系统状态
```
/status
```

### 处理事件
```
/incident
```

## 系统要求

- Claude Code 1.0 或更高版本  
- Kubernetes 命令行工具（kubectl）  
- 已配置集群访问权限  

## 配置说明

请设置 Kubernetes 配置文件路径：
```bash
export KUBECONFIG=~/.kube/config
```

## 示例工作流

```
用户：/deploy production

Claude：
1. 执行 pre-deploy 钩子（校验 kubectl 可用性及集群连接）
2. 交由 deployment-specialist 子智能体执行部署任务
3. 运行 deploy.sh 脚本
4. 通过 Kubernetes MCP 实时监控部署进度
5. 执行 post-deploy 钩子（等待 Pod 就绪、执行冒烟测试）
6. 输出部署摘要报告

结果：
✅ 部署完成  
📦 版本：v2.1.0  
🚀 Pod 状态：3/3 已就绪  
⏱️  耗时：2 分 34 秒
```