# Markdown Translation System

Professional batch translation system for converting English markdown files to Chinese using DashScope API (qwen3.6-plus model).

## Features

- **Type-Aware Translation**: 5 specialized prompt templates for different content types
- **Parallel Processing**: Configurable concurrency (default: 5 files)
- **Resume Capability**: Track progress and restart from last position
- **Comprehensive Logging**: Separate logs for translation, errors, API calls, and progress
- **Error Handling**: Retry logic with exponential backoff
- **Batch Processing**: Process all markdown files in repository

## Installation

```bash
# Install required dependency
pip install httpx

# Or with uv
uv pip install httpx
```

## Configuration

Set your DashScope API key:

```bash
export DASHSCOPE_API_KEY='your-api-key-here'
```

## Usage

### Direct Execution

```bash
# Basic usage
python scripts/markdown_translator.py

# With verbose logging
python scripts/markdown_translator.py --verbose

# Adjust concurrency (default: 5)
python scripts/markdown_translator.py --concurrent 10

# Custom log directory
python scripts/markdown_translator.py --log-dir ./my-logs

# Start fresh (ignore previous progress)
python scripts/markdown_translator.py --no-resume

# Combine options
python scripts/markdown_translator.py --verbose --concurrent 8 --log-dir ./logs
```

### Background Execution with nohup

```bash
# Run in background with nohup
./scripts/run_translation.sh

# Or manually:
nohup python scripts/markdown_translator.py --verbose --concurrent 5 > translation.out 2> translation.err &
```

### Monitoring Progress

```bash
# Watch translation progress
tail -f logs/translation.log

# Check errors
tail -f logs/errors.log

# View API call details
tail -f logs/api_calls.log

# Check progress state
cat logs/progress.json | jq
```

## Translation Types

The system automatically categorizes files and uses specialized prompts:

1. **Main Documentation** (README, CONTRIBUTING, etc.)
   - Style: Professional, welcoming, comprehensive
   - Tone: Authoritative but approachable

2. **Module READMEs** (01-slash-commands/README.md, etc.)
   - Style: Technical guide, structured learning
   - Tone: Instructional, progressive

3. **Slash Commands** (optimize.md, pr.md, etc.)
   - Style: Action-oriented, concise
   - Tone: Direct, practical

4. **Skills Documentation** (SKILL.md files)
   - Style: Technical specification
   - Tone: Precise, detailed

5. **Configuration Examples**
   - Style: Code-commentary hybrid
   - Tone: Technical, explanatory

## Output

- Original: `/path/to/file.md`
- Translation: `/path/to/file_ZH.md` (same directory)

## Log Files

All logs are stored in the specified log directory (default: `./logs/`):

- `translation.log`: Main translation progress and status
- `errors.log`: Error messages and stack traces
- `api_calls.log`: Detailed API request/response data
- `progress.json`: Resume state (completed/failed files)

## Resume Capability

The system automatically saves progress every 5 files. To resume:

```bash
# Just run again - it will automatically resume
python scripts/markdown_translator.py

# To start fresh instead:
python scripts/markdown_translator.py --no-resume
```

## Command-Line Options

```
--root, -r        Root directory to process (default: current directory)
--concurrent, -c  Number of concurrent translations (default: 5)
--log-dir, -l     Log directory (default: ./logs)
--verbose, -v     Enable verbose logging
--no-resume       Start fresh without resuming previous progress
--timeout         API timeout in seconds (default: 30)
```

## Error Handling

- Failed translations are retried 3 times with exponential backoff
- Consistently failing files are skipped and logged
- Progress is saved periodically to prevent data loss
- API errors, network issues, and invalid responses are handled gracefully

## Example Output

```
============================================================
🌏 Markdown Translation System Starting
============================================================
Root directory: /Users/xd/Desktop/codes/claude-howto
Concurrent workers: 5
Resume enabled: True
🔍 Discovering markdown files...
Found 87 files to translate
Resuming: 12 completed, 3 failed
Processing 72 files with concurrency 5
Progress: 1/72 - ✅ 01-slash-commands/README.md
Progress: 2/72 - ✅ 01-slash-commands/optimize.md
Progress: 3/72 - ❌ 01-slash-commands/pr.md
...
============================================================
📊 Translation Complete
============================================================
✅ Successfully translated: 84 files
❌ Failed: 3 files
⏱️  Total time: 1254.32 seconds
📁 Log files: logs/
```

## Troubleshooting

### API Key Errors

```bash
❌ Error: DASHSCOPE_API_KEY environment variable not set
# Fix: export DASHSCOPE_API_KEY='your-key'
```

### Rate Limiting

If you hit API rate limits:
- Reduce concurrency: `--concurrent 3`
- Increase timeout: `--timeout 60`

### Network Issues

For unstable connections:
- Increase timeout: `--timeout 60`
- Check logs for specific errors: `tail -f logs/errors.log`

### Memory Issues

For large repositories:
- Reduce concurrency: `--concurrent 3`
- Process in batches using `--no-resume` after each batch completes

## Requirements

- Python 3.10+
- httpx library
- DashScope API key with qwen3.6-plus access
- Sufficient API quota for batch processing

## Performance

- Average: ~30-60 seconds per file (depends on content length)
- With concurrency 5: ~5-10 files per minute
- 100 files: ~15-20 minutes total
- Network and API response times may vary
