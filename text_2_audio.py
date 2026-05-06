import pyttsx3
import os

def text_2_audio(folder, texter):
    save_path = os.path.join("uploads", folder, "audio.wav")  # use .wav

    engine = pyttsx3.init()

    # optional settings
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # try 0 or 1

    engine.save_to_file(texter, save_path)
    engine.runAndWait()

    print("✅ Audio created (offline)")


