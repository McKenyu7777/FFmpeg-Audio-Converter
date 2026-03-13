# FFmpeg-Audio-Converter

A Python-based CLI tool and standalone executable for batch-converting audio files using the FFmpeg framework.

## Supported Formats

The converter automatically detects and can process the following formats:

* **Input:** `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.m4a`, `.wma`, `.mp4`, `.webm`
* **Output:** * **MP3** (192k bitrate)
* **WAV** (High quality, uncompressed)
* **OGG** (Variable bitrate, -q:a 4)
* **FLAC** (Lossless compression)
* **AAC / M4A / WMA**



## Requirements & Setup

This project was built and tested using **FFmpeg v7.1.1** (Gyan.dev full build).

### For the Python Source Code:

If running the `.py` script directly, you need to install the following dependency:

```bash
pip install pydub

```

**Important:** For the script to function correctly, ensure the following FFmpeg binaries are located in the same folder as the script (or added to your System PATH):

* `ffmpeg.exe`
* `ffplay.exe`
* `ffprobe.exe`

### For the Executable (.exe):

Simply run the `.exe` file. No Python installation or external FFmpeg binaries are required, as they are bundled into the application.

## How to Use

1. **Launch:** Run the `audio_converter.py` or the provided `.exe`.
2. **Step 1:** Paste the full path of the folder containing your source audio files.
3. **Step 2:** Paste the destination path where you want the converted files to be saved.
4. **Step 3:** Select your desired output format from the numbered list (1–7).
5. **Step 4:** Review the summary and press `y` to confirm.

The tool will process the files one by one and provide a success/fail report upon completion. **Note:** Your original files are never deleted; they are kept safe in the source folder.
