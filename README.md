# FFmpeg Audio Converter

A Python CLI tool for batch converting audio files between common formats using **FFmpeg** and **pydub**. Automatically detects audio files in a folder, lets you pick an output format, and converts everything in one go — original files are never touched.

---

## Features

- Batch converts all audio files in a folder to your chosen format
- Auto-detects what audio formats are present in the input folder
- Supports 7 output formats covering all common use cases
- Non-destructive — original files are never modified or deleted
- Available as both a Python script and a standalone `.exe` (no install needed)

---

## Supported Formats

| # | Format | Notes |
|---|--------|-------|
| 1 | MP3 | 192k bitrate, most compatible |
| 2 | WAV | Uncompressed, lossless |
| 3 | OGG | Variable bitrate (-q:a 4), open format |
| 4 | FLAC | Lossless compression |
| 5 | AAC | Good for streaming |
| 6 | M4A | Apple format, good quality |
| 7 | WMA | Windows Media Audio |

**Supported input formats:** `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.m4a`, `.wma`, `.mp4`, `.webm`

---

## Requirements

### Option A — Run the `.exe` (Easiest)
No setup needed. FFmpeg is bundled inside the executable.

Just download and run `audio_converter.exe` — no Python, no FFmpeg install required.

### Option B — Run the Python Script

#### 1. Python 3.x
Download from [python.org](https://www.python.org/downloads/)

#### 2. pydub
```bash
pip install pydub
```

#### 3. FFmpeg
FFmpeg is required for all formats except WAV.

Download the full build from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) — this project was built and tested with **FFmpeg v7.1.1 (full build)**.

**Two ways to set it up:**

**Option 1 — Place FFmpeg next to the script (Recommended)**

Copy these 3 files from the FFmpeg `bin` folder into the same folder as `audio_converter.py`:
```
📁 Your Folder
  ├── audio_converter.py
  ├── ffmpeg.exe
  ├── ffprobe.exe
  └── ffplay.exe
```
The script will automatically detect and use them.

**Option 2 — Add FFmpeg to System PATH**

1. Extract FFmpeg and move the folder somewhere permanent (e.g. `C:\ffmpeg`)
2. Press **Windows + R** → type `sysdm.cpl` → Enter
3. Go to **Advanced** tab → **Environment Variables**
4. Under **System variables**, find **Path** → click **Edit**
5. Click **New** and add the path to the `bin` folder:
   ```
   C:\ffmpeg\bin
   ```
6. Click OK on all windows
7. Open a new CMD and verify with:
   ```
   ffmpeg -version
   ```

---

## Usage

1. Open CMD and navigate to the script folder:
   ```
   cd "D:\Your\Script\Folder"
   ```
2. Run the script:
   ```
   python audio_converter.py
   ```
3. Follow the prompts:
   - **Step 1:** Enter the folder path containing your audio files
   - **Step 2:** Enter the folder path where converted files will be saved
   - **Step 3:** Pick an output format from the numbered list (1–7)
   - **Step 4:** Review the summary and confirm with `y`

### Example Session
```
==================================================
         AUDIO FILE CONVERTER
==================================================

[STEP 1] Enter the folder path containing your audio files:
  Path: D:\Music\Raw

  Detected 6 audio file(s):
    - .wav: 4 file(s)
    - .mp3: 2 file(s)

[STEP 2] Enter the folder path where converted files will be saved:
  Path: D:\Music\Converted

[STEP 3] Choose output format:
  #     Format   Description
  ---------------------------------------------
  1     MP3  - Most common, compressed, smaller file size
  2     WAV  - Uncompressed, high quality, large file size
  3     OGG  - Open format, good compression, good quality
  4     FLAC - Lossless compression, high quality
  5     AAC  - Advanced Audio Coding, good for streaming
  6     M4A  - Apple format, good quality
  7     WMA  - Windows Media Audio

  Enter number (1-7): 3
  Selected: OGG

==================================================
  SUMMARY
==================================================
  Input folder : D:\Music\Raw
  Output folder: D:\Music\Converted
  Output format: OGG
  Files to convert: 6

  Proceed? (y/n): y

==================================================
  Converting 6 file(s) to .OGG
==================================================
  [OK]  track_01.wav  -->  track_01.ogg
  [OK]  track_02.wav  -->  track_02.ogg
  [OK]  song_01.mp3   -->  song_01.ogg
  [OK]  song_02.mp3   -->  song_02.ogg

==================================================
  DONE!
  Successfully converted : 6 file(s)
  Saved to               : D:\Music\Converted
  Original files kept    : YES
==================================================
```

---

## How It Works

1. Scans the input folder and detects all supported audio files
2. Reports what formats were found and how many files per format
3. You pick the output format from the numbered list
4. Each file is loaded via pydub and exported to the target format using FFmpeg under the hood
5. Converted files are saved to your output folder with the same filename but a new extension

---

## Troubleshooting

**`pydub is not installed`**
- Run `pip install pydub` and try again

**MP3 / OGG / FLAC conversion fails**
- FFmpeg is required for these formats
- Make sure `ffmpeg.exe` is either in the same folder as the script or added to your System PATH
- Verify FFmpeg is working by running `ffmpeg -version` in CMD

**`No supported audio files found`**
- Check that your files are directly in the input folder (not in subfolders)
- Supported input formats are: `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.m4a`, `.wma`, `.mp4`, `.webm`

**Access denied / permission error when installing packages**
- Run CMD as Administrator, or use the `--user` flag:
  ```
  pip install pydub --user
  ```

**WARNING: Ignoring invalid distribution messages**
- These are harmless warnings from corrupted leftover temp folders in your Python install
- To fix: navigate to `C:\Python3xx\Lib\site-packages` and delete any folders starting with `~`

---

## Notes

- Files in subfolders are not scanned — all files must be in the root of the input folder
- Output filenames match the original filenames, only the extension changes
- If a file fails to convert, the rest of the batch continues and a fail report is shown at the end
