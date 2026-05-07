--- BEGIN CONTENT ---
---
name: 扩展单元测试
description: 通过测试未覆盖的分支和边界情况来提升测试覆盖率
tags: testing, coverage, unit-tests
---

# 扩展单元测试

在适配项目测试框架的前提下，扩展现有单元测试：

1. **覆盖率分析**：运行覆盖率报告，识别未覆盖的分支、边界情况及低覆盖率区域  
2. **缺口识别**：检查代码中是否存在逻辑分支、错误路径、边界条件，以及 null/空输入等场景  
3. **编写测试**（使用项目所选测试框架）：
   - Jest/Vitest/Mocha（JavaScript/TypeScript）  
   - pytest/unittest（Python）  
   - Go testing/testify（Go）  
   - Rust 测试框架（Rust）  
4. **重点覆盖场景**：  
   - 错误处理与异常捕获  
   - 边界值（最小/最大值、空值、null）  
   - 边缘用例与角落用例（edge/corner cases）  
   - 状态转换与副作用  
5. **验证改进效果**：重新运行覆盖率工具，确认覆盖率有可量化的提升  

仅输出新增的测试代码块；严格遵循项目中已有的测试模式与命名规范。

---
**最后更新**：2026年4月9日

--- END CONTENT ---