# 项目配置

## 项目概览
- **名称**：电子商务平台  
- **技术栈**：Node.js、PostgreSQL、React 18、Docker  
- **团队规模**：5 名开发人员  
- **截止日期**：2025 年第四季度  

## 架构设计  
@docs/architecture.md  
@docs/api-standards.md  
@docs/database-schema.md  

## 开发规范  

### 代码风格  
- 使用 Prettier 进行代码格式化  
- 使用 ESLint（Airbnb 配置）进行代码检查  
- 单行最大长度：100 个字符  
- 缩进使用 2 个空格  

### 命名约定  
- **文件名**：kebab-case（例如 `user-controller.js`）  
- **类名**：PascalCase（例如 `UserService`）  
- **函数/变量名**：camelCase（例如 `getUserById`）  
- **常量名**：UPPER_SNAKE_CASE（例如 `API_BASE_URL`）  
- **数据库表名**：snake_case（例如 `user_accounts`）  

### Git 工作流程  
- 分支命名：`feature/功能描述` 或 `fix/问题描述`  
- 提交信息：遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范  
- 合并前必须创建 Pull Request（PR）  
- 所有 CI/CD 检查必须通过  
- 至少需获得 1 个批准（approval）方可合并  

### 测试要求  
- 代码覆盖率最低为 80%  
- 所有关键业务路径必须覆盖测试用例  
- 单元测试使用 Jest  
- 端到端（E2E）测试使用 Cypress  
- 测试文件命名：`*.test.ts` 或 `*.spec.ts`  

### API 规范  
- 仅提供符合 RESTful 风格的接口  
- 请求与响应均使用 JSON 格式  
- 正确使用 HTTP 状态码  
- 接口版本控制：统一使用 `/api/v1/` 前缀  
- 所有接口须完整文档化，并附带请求/响应示例  

### 数据库  
- 数据库结构变更必须通过迁移脚本（migrations）执行  
- 禁止在代码中硬编码凭据（如数据库密码）  
- 必须启用连接池（connection pooling）  
- 开发环境需开启 SQL 查询日志  
- 必须定期执行数据库备份  

### 部署  
- 基于 Docker 容器化部署  
- 使用 Kubernetes 进行容器编排  
- 采用蓝绿部署（blue-green deployment）策略  
- 部署失败时自动回滚  
- 数据库迁移脚本须在应用部署前执行  

## 常用命令  

| 命令 | 用途 |  
|------|------|  
| `npm run dev` | 启动开发服务器 |  
| `npm test` | 运行全部测试用例 |  
| `npm run lint` | 检查代码风格 |  
| `npm run build` | 构建生产环境包 |  
| `npm run migrate` | 执行数据库迁移 |  

## 团队联系人  
- 技术负责人：Sarah Chen（@sarah.chen）  
- 产品经理：Mike Johnson（@mike.j）  
- DevOps 工程师：Alex Kim（@alex.k）  

## 已知问题及临时解决方案  
- PostgreSQL 连接池在高峰期限制为 20 个连接  
  - 临时方案：实现请求排队机制  
- Safari 14 对 async generator 存在兼容性问题  
  - 临时方案：使用 Babel 进行转译  

## 相关项目  
- 数据分析看板：`/projects/analytics`  
- 移动端应用：`/projects/mobile`  
- 后台管理面板：`/projects/admin`  

---  
**最后更新时间**：2026 年 4 月 9 日