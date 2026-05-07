# 快速入门 — 品牌资源

## 将资源复制到您的项目中

```bash
# 将所有资源复制到您的网站项目中
cp -r resources/ /path/to/your/website/

# 或仅复制网页所需的 favicon
cp resources/favicons/* /path/to/your/website/public/
```

## 在 HTML 中添加（复制粘贴即可）

```html
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## 在 Markdown / 文档中使用

```markdown
# Claude 使用指南

![Claude 使用指南 Logo](resources/logos/claude-howto-logo.svg)

![图标](resources/icons/claude-howto-icon.svg)
```

## 推荐尺寸

| 用途 | 尺寸 | 文件路径 |
|------|------|----------|
| 网站页眉 Logo | 520×120 | `logos/claude-howto-logo.svg` |
| 应用程序图标 | 256×256 | `icons/claude-howto-icon.svg` |
| 浏览器标签页图标 | 32×32 | `favicons/favicon-32.svg` |
| 移动端主屏幕图标 | 128×128 | `favicons/favicon-128.svg` |
| 桌面应用程序图标 | 256×256 | `favicons/favicon-256.svg` |
| 小头像 | 64×64 | `favicons/favicon-64.svg` |

## 颜色定义

```css
/* 可在 CSS 中直接使用 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## 图标设计理念

**带代码括号的罗盘图标**：
- 罗盘圆环 = 导航能力、结构清晰的学习路径  
- 绿色北向指针 = 方向感、进步、引导支持  
- 黑色南向指针 = 基础稳固、坚实根基  
- `>` 符号 = 终端提示符、编程语言、CLI 上下文  
- 刻度标记 = 精准性、步骤分明的指引  

整体象征：“通过结构化编码，以明确指导探索前行之路”。

## 各场景推荐用法

### 网站
- **页眉 Logo**：使用 `logos/claude-howto-logo.svg`  
- **浏览器标签页图标（Favicon）**：使用 `favicons/favicon-32.svg`  
- **社交平台预览图（Social Preview）**：使用 `icons/claude-howto-icon.svg`

### GitHub
- **README 页徽章（Badge）**：使用 64–128px 尺寸的图标  
- **仓库头像（Repository Avatar）**：使用图标文件  

### 社交媒体
- **头像（Avatar）**：使用 256×256px 尺寸的图标  
- **封面图（Banner）**：使用 520×120px 尺寸的 Logo  
- **缩略图（Thumbnail）**：使用 256×256px 尺寸的图标  

### 文档
- **章节标题**：可选用 Logo 或图标（支持缩放）  
- **导航图标**：使用 32–64px 尺寸的 Favicon  

---

完整文档请参阅 [README.md](README.md)。