---  
description: 从源代码生成详尽的 API 文档  
---  

# API 文档生成器  

通过以下步骤生成 API 文档：  

1. 扫描 `/src/api/` 目录下的所有文件  
2. 提取函数签名及 JSDoc 注释  
3. 按端点（endpoint）或模块组织内容  
4. 生成含调用示例的 Markdown 文档  
5. 包含请求/响应数据结构（Schema）  
6. 补充错误处理说明  

输出格式：  
- 输出为 Markdown 文件，路径：`/docs/api.md`  
- 为所有端点提供 `curl` 调用示例  
- 包含 TypeScript 类型定义  

---  
**最后更新**：2026 年 4 月 9 日