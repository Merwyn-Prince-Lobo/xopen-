#!/usr/bin/env bash
# install.sh — installs xopen so you can use it from anywhere
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="/usr/local/bin/xopen"

echo "🔧 Installing xopen..."

# Copy script
sudo cp "$SCRIPT_DIR/xopen.py" "$TARGET"
sudo chmod +x "$TARGET"

# Make sure the shebang works even if python3 is somewhere else
if ! command -v python3 &>/dev/null; then
    echo "❌  python3 not found. Please install Python 3 first."
    exit 1
fi

echo "✅  Done! You can now use:  xopen <file>"
echo ""
echo "Examples:"
echo "  xopen video.mp4"
echo "  xopen document.pdf"
echo "  xopen ."
echo "  xopen ~/Downloads/song.mp3"
