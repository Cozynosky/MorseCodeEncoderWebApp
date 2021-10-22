import os
import time


def cleanup():
    current_time = time.time()
    audio_files_path = os.path.join("static/tmp")
    files = os.listdir(audio_files_path)
    for file in files:
        file_path = os.path.join(f"static/tmp/{file}")
        try:
            creation_time = os.path.getctime(file_path)
            file_life = current_time - creation_time
            if file_life > 60 * 5:
                os.remove(file_path)
        except OSError:
            print(f"Path {file_path} does not exists or is inaccessible")
