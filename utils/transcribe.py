import whisper
import sys

# Load the Whisper model
model = whisper.load_model("tiny")

def get_transcribed_text(file_path):
    if file_path:
        print(f"Audio loaded successfully: {file_path}")
    else:
        print("No file selected.")
        sys.exit(0)

    # Transcribe the audio file
    result = model.transcribe(file_path, language="ne")
    return result