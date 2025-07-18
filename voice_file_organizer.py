
import os
import shutil
from voice_utils import speak

def organize_downloads():
    path = os.path.expanduser("~/Downloads")
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = file.split('.')[-1].lower()
            folder = os.path.join(path, ext + "_files")
            os.makedirs(folder, exist_ok=True)
            shutil.move(full_path, os.path.join(folder, file))
    speak("Downloads organized by file type.")
