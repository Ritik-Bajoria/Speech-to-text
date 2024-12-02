# Whisper Audio Transcription Tool

## Features
- Allows users to select audio files using a file dialog.
- Transcribes audio files into text with high accuracy using the Whisper model.
- Supports various audio file formats including `.mp3`, `.wav`, `.ogg`, and `.flac`.

---

## Requirements

To run this code, you need the following installed on your system:

1. **Python**  
   Ensure Python 3.8 or later is installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Required Python Libraries**  
   Install the required libraries by running the following command in your terminal or command prompt:
   ```bash
   pip install tkinter openai-whisper
   ```

3. **FFmpeg**  
   FFmpeg is required for audio processing. Download and set it up as follows:
   - Download the FFmpeg shared build from this [link](https://web.archive.org/web/20200914201816if_/https://ffmpeg.zeranoe.com/builds/win64/shared/ffmpeg-4.3-win64-shared.zip).
   - Extract the contents of the downloaded `.zip` file to `C:\Program Files`
   - Add the `bin` directory (inside the extracted folder) to your system's PATH environment variable.  
     For example:
     - In Windows, add `C:\Program Files\ffmpeg-4.3-win64-shared\bin` to the PATH variable.

4. **Whisper Model**  
   Whisper will automatically download the necessary model when you run the script for the first time. Ensure you have an active internet connection.

---