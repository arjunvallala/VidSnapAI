# VidSnapAI

VidSnapAI is a simple Python-based project built to practice full-stack development and multimedia processing.

This is not a production-level SaaS, but a basic learning project focused on working with audio, video, and web integration.

The application takes user-provided images and text, converts the text into speech, and combines everything into a short video reel.

---

## Purpose

This project is mainly built for learning:

- Working with Python backend logic  
- Using FFmpeg for video processing  
- Generating audio from text  
- Handling file systems and automation  
- Basic web integration using Flask  

---

## Tech Stack / Libraries Used

- Python  
- Flask (web interface)  
- FFmpeg (video processing)  
- pyttsx3 (text-to-speech, offline)  
- os (file handling)  
- subprocess (running FFmpeg commands)  

---

## Features

- Convert text → audio using pyttsx3  
- Combine images → video using FFmpeg  
- Sync audio with video  
- Generate vertical reels (1080x1920)  
- Simple UI with HTML + CSS  
- Gallery to view generated reels  

---

## Project Structure
```
Reel_Generator/
├── static/
│   ├── reels/                 # generated videos
│   ├── css/
│   └── images/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   ├── gallery.html
│   └── about.html
├── uploads/                   # input data (images + text)
├── main.py                    # Flask app
├── generate_process.py
├── create_reel.py
├── text_2_audio.py
└── done.txt
```


---

## Author

Built as a practice project to improve development skills in Python, multimedia processing, and web integration.
