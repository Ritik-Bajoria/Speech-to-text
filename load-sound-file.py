from tkinter import Tk, filedialog
import sys
import os
import whisper


# Load the Whisper model
model = whisper.load_model("large-v2")
# Function to let the user select an audio file
def select_audio_file():
    # Hide the root tkinter window
    root = Tk()
    root.withdraw()

    # Open a file dialog to select the audio file
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.ogg *.flac"),
            ("All Files", "*.*")
        ]
    )

    return file_path

# Main program
if __name__ == "__main__":
    # Ask the user to select a file
    file_path = select_audio_file()

    if file_path:
        print(f"Audio loaded successfully: {file_path}")
    else:
        print("No file selected.")
        sys.exit(0)

    # Transcribe the audio file
    result = model.transcribe(file_path, language="ne")
    print("Transcribed text:", result["text"])