def create_reel(folder):
    import subprocess
    import os

    input_txt = os.path.join("uploads", folder, "input.txt")
    audio_path = os.path.join("static", "reels", "audio.wav")
    output_path = os.path.join("uploads", folder, "output.mp4")

    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", input_txt,
        "-i", audio_path,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,"
               "pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        "-r", "30",
        "-pix_fmt", "yuv420p",
        output_path
    ]

    print("Running:", " ".join(command))

    subprocess.run(command, check=True)