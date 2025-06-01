# 🎧 MP3 Playlist Cleaner & Scanner

A Python script that **recursively scans your music folders**, filters `.mp3` files based on tags, duration, file size, and naming structure – and creates a **clean `.m3u` playlist**.

Perfect for streamers, radio DJs, or anyone with messy music archives who wants **automated, high-quality playlist generation**.

---

## ✅ Features

- 🔁 **Deep recursive scanning** (all subfolders, unlimited depth, and symbolic links)
- 🎵 Filters only `.mp3` files that are:
  - **> 250 KB**
  - **> 20 seconds**
- 🏷️ Accepts only files with **both `Artist` and `Title` tags**, OR:
- 🧠 **Smart exceptions**:
  - Files inside a folder path containing `musik` and **> 2 MB**
  - Filenames like `Artist - Title.mp3` (even without tags)
- ❌ **Excludes** any files/folders that contain:
  - `kopie`, `samples`, `native instruments`, `whatsapp`, `telegram`
  - (Case-insensitive match)
- 🪵 Logs all scanned folders + unreadable/broken files
- 📂 Saves `.m3u` playlist to a configurable location

---

## 📦 Requirements

- Python 3.x
- [`mutagen`](https://pypi.org/project/mutagen/) library for tag reading

Install with:

```bash
pip install mutagen
```

---

## ▶️ Usage

1. Clone or download this repository
2. Open `playlist.py` in a text editor
3. Adjust the paths and preferences as needed (see below)
4. Run the script:

```bash
python playlist.py
```

---

## 🔧 Customizing the Script

### 1. ✅ Add Your Own Music Folders

Edit this section inside `playlist.py`:

```python
search_paths = [
    r"D:\MyMusic",
    r"E:\Samples\Radio",
    r"H:\ExternalDrive\Music"
]
```

Use raw strings (`r"..."`) and double backslashes if needed.

---

### 2. ✅ Change Playlist Output Location

At the top of the script, modify:

```python
playlist_path = r"D:\cleaned_playlist.m3u"
```

You can also change log file locations:

```python
log_path = r"D:\scan_log.txt"
error_log_path = r"D:\scan_errors.txt"
```

---

### 3. ✅ Adjust Filters (if needed)

Inside the script, you can change:

- **Minimum duration** (`> 20 seconds`)
- **Minimum file size** (`> 250 KB`)
- Accepted extensions (currently `.mp3`)
- Smart filename rule:
  ```python
  if " - " in filename and duration > 20:
  ```

Add or remove filters based on your needs.

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `cleaned_playlist.m3u` | Final playlist with valid `.mp3` files |
| `scan_log.txt`         | All folders that were scanned |
| `scan_errors.txt`      | Files that couldn’t be read (corrupt or missing tags) |
| Console output         | Shows exactly why each file was accepted or skipped |

---

## 🛠 Install Dependencies

Use one of the included installers depending on your OS:

### 🪟 Windows

```bat
install_dependencies.bat
```

### 🐧 Linux / macOS

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

---

## ⚖️ License

This project is licensed under the [Anti-Capitalist Software License v1.4](https://anticapitalist.software).  
You may use, modify, and share this project **only if you do not use it for capitalist ventures or profit generation**.

> *Capitalism not welcome. Radio comrades unite.*

---

## 📻 Made for streamers and radio automation

Created by [Lino Casu](https://github.com/LinoCasu)  
Maintained with ❤️ for music and precision.
