#!/bin/bash
# 🧬 Hive CLI 演示脚本
# 展示 Hive 的基本功能

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HIVE_PY="$SCRIPT_DIR/../src/hive.py"

echo "🧬 Hive CLI 演示"
echo "================"
echo ""

# 清理之前的演示数据
rm -f "$SCRIPT_DIR/../cells/demo-"*.json 2>/dev/null || true

echo "1️⃣  创建蜂房..."
python3 "$HIVE_PY" create-cell demo-japanese
python3 "$HIVE_PY" create-cell demo-medical
python3 "$HIVE_PY" create-cell demo-music
echo ""

echo "2️⃣  列出蜂房..."
python3 "$HIVE_PY" list-cells
echo ""

echo "3️⃣  建立连接..."
python3 "$HIVE_PY" connect demo-japanese demo-medical
python3 "$HIVE_PY" connect demo-medical demo-music
echo ""

echo "4️⃣  查看蜂房详情..."
python3 "$HIVE_PY" show-cell demo-japanese
echo ""

echo "5️⃣  查看生成的文件..."
echo ""
echo "📁 cells/ 目录:"
ls -la "$SCRIPT_DIR/../cells/"
echo ""

echo "📄 demo-japanese.json 内容:"
cat "$SCRIPT_DIR/../cells/demo-japanese.json"
echo ""

echo "✅ 演示完成!"
echo ""
echo "💡 提示:"
echo "   - 查看 README.md 了解更多功能"
echo "   - 运行 'python3 $HIVE_PY help' 查看帮助"
echo "   - 访问 GitHub: https://github.com/vergission-1/hive"
