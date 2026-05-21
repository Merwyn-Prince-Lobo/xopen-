#!/usr/bin/env python3
"""
xopen - Universal file opener
Works on Linux, macOS, and Windows
Usage: xopen <file>   or   xopen .   (to open current directory)
"""

import sys
import os
import subprocess
import platform

# ──────────────────────────────────────────────
#  App mappings per file type
#  Format: extension -> (linux_cmd, mac_cmd, windows_cmd)
#  Use None to fall back to system default
# ──────────────────────────────────────────────
APP_MAP = {
    # Video
    ".mp4":  ("xdg-open", "open", "start"),
    ".mkv":  ("xdg-open", "open", "start"),
    ".mov":  ("xdg-open", "open", "start"),
    ".avi":  ("xdg-open", "open", "start"),
    ".webm": ("xdg-open", "open", "start"),
    ".flv":  ("xdg-open", "open", "start"),

    # Audio
    ".mp3":  ("xdg-open", "open", "start"),
    ".wav":  ("xdg-open", "open", "start"),
    ".flac": ("xdg-open", "open", "start"),
    ".ogg":  ("xdg-open", "open", "start"),
    ".aac":  ("xdg-open", "open", "start"),
    ".m4a":  ("xdg-open", "open", "start"),

    # Documents
    ".pdf":  ("xdg-open", "open", "start"),
    ".docx": ("xdg-open", "open", "start"),
    ".doc":  ("xdg-open", "open", "start"),
    ".xlsx": ("xdg-open", "open", "start"),
    ".pptx": ("xdg-open", "open", "start"),

    # Images
    ".jpg":  ("xdg-open", "open", "start"),
    ".jpeg": ("xdg-open", "open", "start"),
    ".png":  ("xdg-open", "open", "start"),
    ".gif":  ("xdg-open", "open", "start"),
    ".svg":  ("xdg-open", "open", "start"),
    ".webp": ("xdg-open", "open", "start"),

    # Code / Text (opens in default editor)
    ".txt":  ("xdg-open", "open", "start"),
    ".md":   ("xdg-open", "open", "start"),
    ".json": ("xdg-open", "open", "start"),
    ".py":   ("xdg-open", "open", "start"),
    ".js":   ("xdg-open", "open", "start"),
    ".html": ("xdg-open", "open", "start"),
    ".css":  ("xdg-open", "open", "start"),

    # Archives
    ".zip":  ("xdg-open", "open", "start"),
    ".tar":  ("xdg-open", "open", "start"),
    ".gz":   ("xdg-open", "open", "start"),
    ".rar":  ("xdg-open", "open", "start"),
    ".7z":   ("xdg-open", "open", "start"),
}

COLORS = {
    "green":  "\033[92m",
    "red":    "\033[91m",
    "yellow": "\033[93m",
    "cyan":   "\033[96m",
    "bold":   "\033[1m",
    "reset":  "\033[0m",
}

def c(color, text):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

def get_os():
    s = platform.system()
    if s == "Linux":   return "linux"
    if s == "Darwin":  return "mac"
    if s == "Windows": return "windows"
    return "linux"  # fallback

def open_file(path):
    os_name = get_os()
    idx     = {"linux": 0, "mac": 1, "windows": 2}[os_name]

    path = os.path.abspath(path)

    # Directory → open file manager
    if os.path.isdir(path):
        print(c("cyan", f"📂 Opening directory: {path}"))
        cmd = {"linux": "xdg-open", "mac": "open", "windows": "explorer"}[os_name]
        _run([cmd, path], os_name)
        return

    if not os.path.exists(path):
        print(c("red", f"✗  File not found: {path}"))
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    entry = APP_MAP.get(ext)

    if entry is None:
        print(c("yellow", f"⚠  Unknown extension '{ext}', trying system default..."))
        cmd = {"linux": "xdg-open", "mac": "open", "windows": "start"}[os_name]
    else:
        cmd = entry[idx]

    print(c("green", f"▶  Opening {c('bold', os.path.basename(path))}"))
    _run([cmd, path], os_name)

def _run(cmd_list, os_name):
    try:
        if os_name == "windows":
            # 'start' is a shell built-in on Windows
            subprocess.Popen(cmd_list, shell=True,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(cmd_list,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(c("red", f"✗  Command '{cmd_list[0]}' not found on your system."))
        print(   "   Try installing it or set a custom app in xopen.py → APP_MAP")
        sys.exit(1)

def usage():
    print(f"""
{c('bold', 'xopen')} — universal file opener

{c('cyan', 'Usage:')}
  xopen <file>          open any file
  xopen .               open current directory
  xopen path/to/dir     open a directory

{c('cyan', 'Supported types:')}
  video   mp4 mkv mov avi webm flv
  audio   mp3 wav flac ogg aac m4a
  docs    pdf docx xlsx pptx
  images  jpg png gif svg webp
  code    py js html css json md txt
  zip     zip tar gz rar 7z
  + anything else → tries system default
""")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        usage()
        sys.exit(0)

    target = sys.argv[1]

    # Special: "." means current dir
    if target == ".":
        target = os.getcwd()

    open_file(target)

if __name__ == "__main__":
    main()
