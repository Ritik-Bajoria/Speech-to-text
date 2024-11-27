from pydub import AudioSegment
from tkinter import Tk, filedialog
from pydub.utils import which
ffmpeg_path = which("ffmpeg")
ffprobe_path = which("ffprobe")

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
        try:
            # Load the selected audio file
            audio = AudioSegment.from_file(file_path)
            print(f"Audio loaded successfully: {file_path}")
            print(f"Duration: {len(audio)} ms, Channels: {audio.channels}")
        except Exception as e:
            print(f"Error loading audio file: {e}")
    else:
        print("No file selected.")
