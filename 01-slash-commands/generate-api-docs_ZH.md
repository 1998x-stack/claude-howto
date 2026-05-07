---  
description: 从源代码生成全面的 API 文档  
---  

# API 文档生成器  

通过以下步骤生成 API 文档：  

1. 扫描 `/src/api/` 目录下的所有文件  
2. 提取函数签名及 JSDoc 注释  
3. 按端点（endpoint）或模块组织内容  
4. 以 Markdown 格式生成文档，并附带调用示例  
5. 包含请求与响应的数据结构（schema）  
6. 补充错误处理说明  

输出格式：  
- 生成 Markdown 文件至 `/docs/api.md`  
- 为所有端点提供 `curl` 调用示例  
- 包含对应的 TypeScript 类型定义  

---  
**最后更新时间**：2026 年 4 月 9 日