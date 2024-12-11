import os
import sys
from tkinter import Tk, filedialog

def select_audio_file():
    file_path = None

    # Check if a GUI is available
    if sys.platform == "linux" and not os.environ.get("DISPLAY"):
        # If no DISPLAY environment variable is set, assume no GUI
        print("No GUI available. Please enter the file path manually:")
        file_path = input("Enter the path to the audio file: ")
    else:
        try:
            # Try to create a Tkinter GUI window
            root = Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="Select an Audio File",
                filetypes=[
                    ("Audio Files", "*.mp3 *.wav *.ogg *.flac"),
                    ("All Files", "*.*")
                ]
            )
        except Exception as e:
            # to manually ask for a file path in case error occurs while opening file dialog
            print(f"An error occurred while opening the file dialog: {e}")
            print("Please enter the file path manually:")
            file_path = input("Enter the path to the audio file: ")
        finally:
            # to ensure that the root tkinter window is properly closed 
            # and any associated resources are released 
            if 'root' in locals():
                root.destroy()

    return file_path
