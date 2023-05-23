# Google Bard Voice Activated Assistant
Google AI BARD powered Python voice assistant. Implements a free Bard API and OpenAI Whisper for local transcribing.

## YouTube tutorial and preview
https://youtu.be/vfbmlRSgj9Q

<span style="color:orange">NOTE: Open AI whisper will not run on Python versions newer than 3.10. Python 3.11 and newer will not run this program.
## Authentication
Sign into your account with Bard access at https://bard.google.com/
- F12 for developer console
- Copy the values
  - Session: Go to Application → Cookies → `__Secure-1PSID`. Copy the value of that cookie.

## Installation
Clone GitHub repo.
```bash
git clone url
```
Change directory to bard_voice.
```bash
cd bard_voice
```
Paste your Bard Token into line 10 of the main.py file, replacing {YOUR BARD TOKEN}.
```bash
token = "{YOUR BARD TOKEN}"
```

Install Python dependencies (use pip3 if your system requires).
```bash
pip install -r requirements.txt
```
Whisper requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```
## Startup Voice Assistant
```bash
python main.py
```
