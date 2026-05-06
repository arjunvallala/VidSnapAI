import os
import time
import text_2_audio
import subprocess


def process_folder(folder):
    path = os.path.join("uploads", folder, "desc.txt")

    if not os.path.exists(path):
        print(f"❌ desc.txt missing in {folder}")
        return

    with open(path) as f:
        text = f.read().strip()

    if not text:
        print(f"⚠️ Empty text in {folder}")
        return

    # Step 1: Audio
    text_2_audio.text_2_audio(folder, text)

    #Step 2: Video
    create_reel(folder)

def create_reel(folder):
    reels_dir = os.path.join("static", "reels")
    os.makedirs(reels_dir, exist_ok=True)
    input_txt = os.path.join("uploads", folder, "input.txt")
    audio_path = os.path.join("uploads", folder, "audio.wav")
    output_path = os.path.join("static", "reels", f"{folder}.mp4")
    

    command = [
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", input_txt,
    "-i", audio_path,

    # 🔥 IMPORTANT FIX
    "-map", "0:v:0",
    "-map", "1:a:0",

    "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,"
           "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",

    "-c:v", "libx264",
    "-c:a", "aac",

    "-shortest",
    "-r", "30",
    "-pix_fmt", "yuv420p",

    output_path
    ]
    subprocess.run(command)

if __name__ == "__main__":
    with open("done.txt","r") as f:
        done_folders = f.readlines()
    folders = os.listdir("uploads")
    for folder in folders:
        if(folder not in done_folders):
            process_folder(folder)
            with open("done.txt","a") as f:
                f.write(folder)
        else:
            print(f"Reel is already created for {folder}")

    time.sleep(10)  # slower loop