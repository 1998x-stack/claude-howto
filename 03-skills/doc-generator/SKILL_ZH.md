--- BEGIN CONTENT ---
---
name: api-documentation-generator
description: 从源代码生成全面、准确的 API 文档。适用于创建或更新 API 文档、生成 OpenAPI 规范，或当用户提及 API 文档、端点或相关文档时。
---

# API 文档生成器技能

## 生成内容

- OpenAPI / Swagger 规范  
- API 端点文档  
- SDK 使用示例  
- 集成指南  
- 错误码参考  
- 认证使用指南  

## 文档结构

### 每个端点的文档格式

```markdown
## GET /api/v1/users/:id

### 描述
对该端点功能的简要说明

### 参数

| 名称 | 类型 | 是否必需 | 描述 |
|------|------|----------|------|
| id | 字符串 | 是 | 用户 ID |

### 响应

**200 成功**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 未找到**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "用户不存在"
}
```

### 示例

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```
```