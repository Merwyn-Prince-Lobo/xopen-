# xopen — Universal File Opener

One command to open anything. Works on **Linux**, **macOS**, and **Windows**.

## Install

### Linux / macOS
```bash
chmod +x install.sh
./install.sh
```

### Windows (run as Admin)
```
install.bat
```

## Usage

```bash
xopen video.mp4          # opens in your default video player
xopen song.mp3           # opens in your default audio player
xopen document.pdf       # opens in your PDF viewer
xopen image.png          # opens in your image viewer
xopen script.py          # opens in your default editor
xopen .                  # opens current folder in file manager
xopen ~/Downloads        # opens any directory
```

## Supported File Types

| Category | Extensions |
|----------|------------|
| Video    | mp4 mkv mov avi webm flv |
| Audio    | mp3 wav flac ogg aac m4a |
| Docs     | pdf docx xlsx pptx doc |
| Images   | jpg png gif svg webp |
| Code     | py js html css json md txt |
| Archives | zip tar gz rar 7z |

Anything not in the list? It falls back to your system default.

## Customize

Open `xopen.py` and edit the `APP_MAP` dict to force specific apps:

```python
# Example: always open .pdf with zathura instead of default
".pdf": ("zathura", "open", "start"),
```
