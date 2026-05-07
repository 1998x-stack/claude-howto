# API 模块标准

本文件覆盖 `/src/api/` 目录下的根级 `CLAUDE.md` 文件。

## API 专用标准

### 请求验证
- 使用 [Zod](https://zod.dev/) 进行数据结构验证；
- 始终验证所有入参数据；
- 验证失败时返回 HTTP 状态码 `400`，并附带具体错误信息；
- 错误响应需按字段级别提供详细错误信息。

### 身份认证
- 所有端点均需携带 JWT 访问令牌；
- 令牌通过 `Authorization` 请求头传递（格式为 `Bearer <token>`）；
- 访问令牌有效期为 24 小时；
- 实现刷新令牌（Refresh Token）机制以支持无感续期。

### 响应格式

所有成功响应必须遵循以下 JSON 结构：

```json
{
  "success": true,
  "data": { /* 实际业务数据 */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

错误响应格式如下：

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "面向用户的提示信息",
    "details": { /* 字段级错误详情 */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### 分页（Pagination）
- 采用基于游标（Cursor-based）的分页方式，**不使用偏移量（offset/limit）**；
- 响应中必须包含布尔字段 `hasMore`，用于标识是否还有更多数据；
- 单页最大条目数：100；
- 默认每页条目数：20。

### 请求频率限制（Rate Limiting）
- 已认证用户：每小时最多 1000 次请求；
- 公共端点（无需认证）：每小时最多 100 次请求；
- 超出限额时返回 HTTP 状态码 `429 Too Many Requests`；
- 响应头中必须包含 `Retry-After`，指示可重试时间（单位：秒）。

### 缓存（Caching）
- 使用 Redis 存储会话及高频读取数据；
- 默认缓存有效期：5 分钟；
- 在执行写操作（如创建、更新、删除）后立即使相关缓存失效；
- 缓存键（Cache Key）需按资源类型打标签（例如：`user:123`、`post:list:cursor:abc`），便于批量清理。

---
**最后更新日期**：2026 年 4 月 9 日