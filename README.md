# VidSnapAI
VidSnapAI is an AI-powered reel generator that converts images and text into engaging short videos. It uses text-to-speech for narration and FFmpeg for video processing, allowing users to automatically create ready-to-share reels with minimal effort.
VidSnapAI

VidSnapAI is a simple Python-based project built to practice full-stack development and multimedia processing.
This is not a production-level SaaS, but a basic project created to improve skills in handling audio, video, and web integration.

The application takes user-provided images and text, converts the text into speech, and combines everything into a short video reel.

Purpose

This project is mainly built for learning:

Working with Python backend logic
Using FFmpeg for video processing
Generating audio from text
Handling file systems and automation
Basic web integration using Flask
Tech Stack / Libraries Used
Python
Flask (for web interface)
FFmpeg (video processing)
pyttsx3 (text-to-speech, offline)
OS module (file handling)
Subprocess (running FFmpeg commands)
Features
Convert text → audio using pyttsx3
Combine images → video using FFmpeg
Automatically sync audio with video
Generate vertical reels (1080x1920)
Simple UI with templates (HTML + CSS)
Basic gallery to view generated reels
Project Structure
Reel_Generator/
│
├── static/
│   ├── reels/        # generated videos
│   ├── css/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   ├── gallery.html
│   └── about.html
│
├── uploads/          # input data (images + text)
│
├── main.py           # Flask app
├── generate_process.py
├── create_reel.py
├── text_2_audio.py
└── done.txt
Requirements

Make sure you have:

Python 3.x
FFmpeg installed and added to PATH

Check FFmpeg:

ffmpeg -version
Installation

Clone the repository:

git clone https://github.com/your-username/VidSnapAI.git
cd VidSnapAI

Install dependencies:

pip install flask pyttsx3
How to Run
Step 1: Start Flask app
python main.py
Step 2: Run processing script (in another terminal)
python generate_process.py
How it Works
User uploads images + text
Text is converted to audio using pyttsx3
FFmpeg reads images and creates video
Audio is merged with video
Output is saved in:
static/reels/
Notes
This is a learning project, not optimized for production
Error handling is basic
Processing may be slow depending on system
FFmpeg must be properly installed or video generation will fail
Future Improvements (optional)
Better UI/UX
Async processing
Cloud storage
Better audio quality
Deployment support
Author

Built as a practice project to improve development skills in Python, multimedia processing, and web integration.
