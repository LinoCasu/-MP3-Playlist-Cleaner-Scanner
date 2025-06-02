import os
from mutagen import File
from mutagen.mp3 import MP3

# Folders to scan
search_paths = [
    r"C:\User\linoc\OneDrive\Musik",
    r"H:\ONEDRIVE\Musik",
    r"H:\ONEDRIVE\Musik\BACKUP\BACKUP",
    r"D:\\",
    r"H:\\"
]

# Output files
playlist_path = r"D:\cleaned_playlist.m3u"
log_path = r"D:\scan_log.txt"
error_log_path = r"D:\scan_errors.txt"
non_mp3_log_path = r"D:\non_mp3_report.txt"

valid_files = []

# Clean old output files
for file_path in [playlist_path, log_path, error_log_path, non_mp3_log_path]:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except PermissionError:
        print(f"⚠️ Cannot delete {file_path} – is it open?")
        continue

print("🔍 Starting deep scan...\n")

for path in search_paths:
    for root, dirs, files in os.walk(path, followlinks=True):
        try:
            with open(log_path, "a", encoding="utf-8") as log:
                log.write(f"{root}\n")
        except PermissionError:
            print(f"❌ Cannot write to log file: {log_path}")
            continue

        for file in files:
            full_path = os.path.join(root, file)
            full_path_lower = full_path.lower()

            if (
                not full_path_lower.endswith(".mp3")
                or "kopie" in full_path_lower
                or "samples" in full_path_lower
                or "native instruments" in full_path_lower
                or "whatsapp" in full_path_lower
                or "telegram" in full_path_lower
            ):
                print("🚫 Skipped (exclusion rule):", full_path)
                continue

            try:
                audio_check = File(full_path)
                if not audio_check or not audio_check.mime or "audio/mpeg" not in audio_check.mime:
                    with open(non_mp3_log_path, "a", encoding="utf-8") as report:
                        report.write(full_path + "\n")
                    print("❌ Not a valid MP3 (MIME):", full_path)
                    continue

                size_kb = os.path.getsize(full_path) / 1024
                if size_kb < 250:
                    print("❌ Too small (<250KB):", full_path)
                    continue

                audio = MP3(full_path)
                tags = audio.tags
                duration = audio.info.length if audio.info else 0

                if tags:
                    artist = tags.get("TPE1")
                    title = tags.get("TIT2")
                    if artist and title and duration > 20:
                        print("✅ Accepted (tagged):", full_path)
                        valid_files.append(full_path)
                        continue
                    else:
                        print("❌ Incomplete tags:", full_path)

                if "musik" in full_path_lower and size_kb > 2048 and duration > 20:
                    print("ℹ️ Accepted by path/size rule:", full_path)
                    valid_files.append(full_path)
                    continue

                filename = os.path.basename(full_path)
                if " - " in filename and duration > 20:
                    print("🎯 Accepted by filename pattern:", full_path)
                    valid_files.append(full_path)
                    continue

                print("❌ Rejected (no condition matched):", full_path)

            except Exception:
                with open(error_log_path, "a", encoding="utf-8") as error_log:
                    error_log.write(f"Error reading file: {full_path}\n")
                print("⚠️ Error reading file:", full_path)

# --- FINAL CLEANING PASS ---
final_valid_files = []
unwanted_extensions = [
    ".zip", ".rar", ".7z", ".tar", ".gz", ".php", ".html", ".htm", ".txt",
    ".ini", ".bak", ".pdf", ".docx", ".csv", ".json"
]
unwanted_folders = [
    "wp-content", "updraft", "backup\\backup", "wordpress", "temp", "cache", "web", "site"
]

for track in valid_files:
    track_lower = track.lower()
    if any(track_lower.endswith(ext) for ext in unwanted_extensions):
        print("🧹 Removed (unwanted extension):", track)
        continue
    if any(bad_folder in track_lower for bad_folder in unwanted_folders):
        print("🧹 Removed (unwanted folder):", track)
        continue
    final_valid_files.append(track)

print(f"\n✅ Final valid entries: {len(final_valid_files)} files")
print(f"💾 Writing cleaned playlist to: {playlist_path}")

try:
    with open(playlist_path, "w", encoding="utf-8") as f:
        for track in final_valid_files:
            f.write(track + "\n")
    print("🎉 Final cleaned playlist saved.")
except Exception as e:
    print(f"❌ Failed to write playlist: {e}")
