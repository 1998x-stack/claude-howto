#!/bin/bash
# nohup runner for markdown translation system

set -e

LOG_DIR="./translation_logs"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

if [ -z "$DASHSCOPE_API_KEY" ]; then
    echo "❌ Error: DASHSCOPE_API_KEY environment variable not set"
    echo "Please set it first: export DASHSCOPE_API_KEY='your-api-key'"
    exit 1
fi

echo "🌏 Starting Markdown Translation System"
echo "======================================"
echo "API Key: ${DASHSCOPE_API_KEY:0:10}..."
echo "Log Directory: $LOG_DIR"
echo "Timestamp: $TIMESTAMP"
echo ""

mkdir -p "$LOG_DIR"

nohup python3 scripts/markdown_translator.py \
    --verbose \
    --concurrent 5 \
    --log-dir "$LOG_DIR" \
    > "$LOG_DIR/translation_$TIMESTAMP.out" \
    2> "$LOG_DIR/translation_$TIMESTAMP.err" &

PID=$!

echo "✅ Translation process started in background"
echo "Process ID: $PID"
echo ""
echo "📁 Log Files:"
echo "  - Main log: $LOG_DIR/translation_$TIMESTAMP.out"
echo "  - Error log: $LOG_DIR/translation_$TIMESTAMP.err"
echo "  - Translation log: $LOG_DIR/translation.log"
echo "  - API log: $LOG_DIR/api_calls.log"
echo "  - Progress: $LOG_DIR/progress.json"
echo ""
echo "🔍 Monitor progress:"
echo "  tail -f $LOG_DIR/translation.log"
echo ""
echo "🛑 Stop translation:"
echo "  kill $PID"
echo ""
echo "📊 Check status:"
echo "  ps aux | grep $PID"

# Save PID for easy reference
echo $PID > "$LOG_DIR/translation.pid"

exit 0
