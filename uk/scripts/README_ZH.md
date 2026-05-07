<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude 使用指南" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 构建脚本

从 Claude How-To 的 Markdown 文件构建 EPUB 格式电子书。

## 功能特性

- 按目录结构组织章节（如 `01-slash-commands`、`02-memory` 等）
- 通过 Kroki.io API 将 Mermaid 图表渲染为 PNG 图像
- 异步并行加载 —— 同时渲染所有图表
- 基于项目 Logo 自动生成封面
- 将文档内 Markdown 链接自动转换为 EPUB 内部章节链接
- 严格错误模式：若任一图表无法成功渲染，则构建过程立即中止

## 系统要求

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv)
- 网络连接（用于 Mermaid 图表远程渲染）

## 快速开始

```bash
# 最简方式 —— uv 自动处理全部依赖
uv run scripts/build_epub.py
```

## 开发环境配置

```bash
# 创建虚拟环境
uv venv

# 激活环境并安装开发依赖
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# 运行测试
pytest scripts/tests/ -v

# 执行构建脚本
python scripts/build_epub.py
```

## 命令行参数

```
用法: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

选项:
  -h, --help            显示此帮助信息并退出
  --root, -r ROOT       项目根目录（默认：仓库根目录）
  --output, -o OUTPUT   输出路径（默认：claude-howto-guide.epub）
  --verbose, -v         启用详细日志输出
  --timeout TIMEOUT     API 请求超时时间（秒，默认：30）
  --max-concurrent N    最大并发请求数（默认：10）
```

## 使用示例

```bash
# 启用详细日志输出构建
uv run scripts/build_epub.py --verbose

# 指定自定义输出路径
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 限制并发请求数（适用于遭遇限流时）
uv run scripts/build_epub.py --max-concurrent 5
```

## 输出结果

在仓库根目录下生成 `claude-howto-guide.epub` 文件。

EPUB 包含以下内容：
- 带项目 Logo 的封面
- 支持嵌套章节的完整目录
- 全部 Markdown 内容已转换为符合 EPUB 规范的 HTML
- 所有 Mermaid 图表均已渲染为 PNG 图像并嵌入

## 运行测试

```bash
# 使用虚拟环境运行
source .venv/bin/activate
pytest scripts/tests/ -v

# 或直接使用 uv 运行（自动管理依赖）
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## 依赖项

依赖关系通过 PEP 723 内联脚本元数据统一管理：

| 包名 | 用途 |
|------|------|
| `ebooklib` | EPUB 文件生成 |
| `markdown` | Markdown → HTML 转换 |
| `beautifulsoup4` | HTML 解析与操作 |
| `httpx` | 异步 HTTP 客户端 |
| `pillow` | 封面图像生成 |
| `tenacity` | 重试逻辑（网络请求容错） |

## 故障排查

**构建因网络错误失败**：请检查网络连接及 [Kroki.io](https://kroki.io) 服务状态；可尝试增加超时时间：`--timeout 60`。

**遭遇速率限制（Rate Limiting）**：请降低并发数，例如：`--max-concurrent 3`。

**缺少 Logo 文件**：若未找到 `claude-howto-logo.png`，脚本将自动生成纯文本封面。