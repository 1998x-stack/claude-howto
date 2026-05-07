# 快速开始 — 品牌资源

## 将资源复制到您的项目中

```bash
# 将所有资源复制到您的网站项目中
cp -r resources/ /path/to/your/website/

# 或仅复制网页所需的 favicon
cp resources/favicons/* /path/to/your/website/public/
```

## 添加至 HTML（直接复制粘贴）

```html
<!-- Favicons -->
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

| 用途 | 尺寸 | 文件 |
|------|------|------|
| 网站页眉 | 520×120 | `logos/claude-howto-logo.svg` |
| 应用图标 | 256×256 | `icons/claude-howto-icon.svg` |
| 浏览器标签页 | 32×32 | `favicons/favicon-32.svg` |
| 移动端主屏幕 | 128×128 | `favicons/favicon-128.svg` |
| 桌面应用图标 | 256×256 | `favicons/favicon-256.svg` |
| 小型头像 | 64×64 | `favicons/favicon-64.svg` |

## 颜色值

```css
/* 可在 CSS 中直接使用 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## 图标设计含义

**带代码括号的指南针**：
- 指南针圆环 = 导航、结构化的学习路径  
- 绿色指北针 = 方向、进步与引导  
- 黑色指南针南端 = 扎实根基与稳定性  
- `>` 括号 = 终端提示符、编程、命令行环境  
- 刻度线 = 精确性与结构化步骤  

该符号寓意：“以清晰指引，助你畅游代码世界。”

## 各场景推荐用法

### 网站
- **页眉**：Logo（`logos/claude-howto-logo.svg`）  
- **网站图标（Favicon）**：32px（`favicons/favicon-32.svg`）  
- **社交平台预览图**：图标（`icons/claude-howto-icon.svg`）

### GitHub
- **README 中的徽章**：图标（`icons/claude-howto-icon.svg`），建议尺寸 64–128px  
- **仓库头像**：图标（`icons/claude-howto-icon.svg`）

### 社交媒体
- **个人资料头像**：图标（`icons/claude-howto-icon.svg`）  
- **封面图（Banner）**：Logo（`logos/claude-howto-logo.svg`）  
- **缩略图（Thumbnail）**：图标（256×256px）

### 文档
- **章节标题**：Logo 或图标（按需缩放适配）  
- **导航图标**：Favicon（32–64px）

---

完整说明请参阅 [README.md](README.md)。