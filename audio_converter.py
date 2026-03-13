import os
import sys
from pathlib import Path

def check_pydub():
    try:
        from pydub import AudioSegment
        return AudioSegment
    except ImportError:
        print("ERROR: pydub is not installed. Run: pip install pydub")
        sys.exit(1)

def get_supported_formats():
    return {
        "1": ("mp3",  "MP3  - Most common, compressed, smaller file size"),
        "2": ("wav",  "WAV  - Uncompressed, high quality, large file size"),
        "3": ("ogg",  "OGG  - Open format, good compression, good quality"),
        "4": ("flac", "FLAC - Lossless compression, high quality"),
        "5": ("aac",  "AAC  - Advanced Audio Coding, good for streaming"),
        "6": ("m4a",  "M4A  - Apple format, good quality"),
        "7": ("wma",  "WMA  - Windows Media Audio"),
    }

def detect_audio_files(folder_path):
    supported_input = [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma", ".mp4", ".webm"]
    found = {}
    files = []

    for file in Path(folder_path).iterdir():
        if file.is_file() and file.suffix.lower() in supported_input:
            ext = file.suffix.lower().replace(".", "")
            found[ext] = found.get(ext, 0) + 1
            files.append(file)

    return files, found

def convert_files(files, output_path, output_format, AudioSegment):
    os.makedirs(output_path, exist_ok=True)
    success = 0
    failed = 0

    print(f"\n{'='*50}")
    print(f"  Converting {len(files)} file(s) to .{output_format.upper()}")
    print(f"{'='*50}")

    for file in files:
        try:
            output_file = Path(output_path) / (file.stem + f".{output_format}")

            # Load audio (detect format from extension)
            ext = file.suffix.lower().replace(".", "")
            audio = AudioSegment.from_file(str(file), format=ext)

            # Export with format-specific settings
            export_params = {}
            if output_format == "mp3":
                export_params = {"bitrate": "192k"}
            elif output_format == "ogg":
                export_params = {"parameters": ["-q:a", "4"]}
            elif output_format == "flac":
                export_params = {}

            audio.export(str(output_file), format=output_format, **export_params)
            print(f"  [OK]  {file.name}  -->  {output_file.name}")
            success += 1

        except Exception as e:
            print(f"  [FAIL] {file.name} - Error: {e}")
            failed += 1

    return success, failed

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)
    print("         AUDIO FILE CONVERTER")
    print("=" * 50)

    AudioSegment = check_pydub()
    formats = get_supported_formats()

    # --- Step 1: Input folder ---
    while True:
        print("\n[STEP 1] Enter the folder path containing your audio files:")
        input_path = input("  Path: ").strip().strip('"')

        if not os.path.exists(input_path):
            print(f"  ERROR: Path does not exist. Try again.")
            continue

        files, detected = detect_audio_files(input_path)

        if not files:
            print("  ERROR: No supported audio files found in that folder.")
            continue

        print(f"\n  Detected {len(files)} audio file(s):")
        for fmt, count in detected.items():
            print(f"    - .{fmt}: {count} file(s)")
        break

    # --- Step 2: Output folder ---
    print("\n[STEP 2] Enter the folder path where converted files will be saved:")
    output_path = input("  Path: ").strip().strip('"')

    # --- Step 3: Output format ---
    print("\n[STEP 3] Choose output format:")
    print(f"  {'#':<5} {'Format':<8} Description")
    print(f"  {'-'*45}")
    for key, (fmt, desc) in formats.items():
        print(f"  {key:<5} {desc}")

    while True:
        choice = input("\n  Enter number (1-7): ").strip()
        if choice in formats:
            output_format = formats[choice][0]
            print(f"  Selected: {output_format.upper()}")
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 7.")

    # --- Step 4: Confirm ---
    print(f"\n{'='*50}")
    print(f"  SUMMARY")
    print(f"{'='*50}")
    print(f"  Input folder : {input_path}")
    print(f"  Output folder: {output_path}")
    print(f"  Output format: {output_format.upper()}")
    print(f"  Files to convert: {len(files)}")
    confirm = input("\n  Proceed? (y/n): ").strip().lower()

    if confirm != "y":
        print("\n  Cancelled.")
        sys.exit(0)

    # --- Step 5: Convert ---
    success, failed = convert_files(files, output_path, output_format, AudioSegment)

    # --- Done ---
    print(f"\n{'='*50}")
    print(f"  DONE!")
    print(f"  Successfully converted : {success} file(s)")
    if failed:
        print(f"  Failed                 : {failed} file(s)")
    print(f"  Saved to               : {output_path}")
    print(f"  Original files kept    : YES")
    print(f"{'='*50}")
    input("\n  Press Enter to exit...")

if __name__ == "__main__":
    main()
