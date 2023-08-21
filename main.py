from Bard import Chatbot
from playsound import playsound
import speech_recognition as sr
from os import system
import whisper
import warnings
import sys

# Paste your Bard Token (check README.md for where to find yours) 
token = 'Replace with your __Secure-1PSID value.'
ts_token = 'Replace with your __Secure-1PSIDTS value.'
# Initialize Google Bard API
chatbot = Chatbot(token, ts_token)
# Initialize speech recognition
r = sr.Recognizer()
# Initialize Whisper model
tiny_model = whisper.load_model('tiny')
base_model = whisper.load_model('base')

# Initiate pyttsx3 if not running Mac OS
if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 
    # Get the current speech rate
    rate = engine.getProperty('rate')
    # Decrease speech rate by 50 words per minute (Change as desired)
    engine.setProperty('rate', rate-50) 

def prompt_bard(prompt):
    response = chatbot.ask(prompt)
    return response['content']

def speak(text):
    # If Mac OS use system messages for TTS
    if sys.platform == 'darwin':
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$: ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    # Use pyttsx3 for other operating sytstems
    else:
        engine.say(text)
        engine.runAndWait()

def main():
    # Initialize microphone object
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # Runs program indefinitely
        while True:
            # Continuously listens for wake word locally
            while True:
                try:
                    print('\nSay "google" to wake me up. \n')
                    audio = r.listen(source)
                    with open("wake_detect.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                    # Transcribe wake word using whisper tiny model
                    result = tiny_model.transcribe('wake_detect.wav')
                    text_input = result['text']
                    # If wake word is found, break out of loop
                    if 'google' in text_input.lower().strip():
                        break
                    else:
                        print("No wake word found. Try again.")
                except Exception as e:
                    print("Error transcribing audio: ", e)
                    continue
            try:
                # Play wake word detected notification sound (faster than TTS)
                playsound('wake_detected.mp3')
                print("Wake word detected. Please speak your prompt to Bard. \n")
                # Record prompt
                audio = r.listen(source)
                with open("prompt.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                # Transcribe prompt using whisper base model
                result = base_model.transcribe('prompt.wav')
                prompt_text = result['text']
                print("Sending to Bard:", prompt_text, '\n')
                # If prompt is empty, start listening for wake word again
                if len(prompt_text.strip()) == 0:
                    print("Empty prompt. Please speak again.")
                    speak("Empty prompt. Please speak again.")
                    continue
            except Exception as e:
                print("Error transcribing audio: ", e)
                continue
            # Prompt Bard. 
            response = prompt_bard(prompt_text)
            # Prints Bard response normal if windows (cannot ASCII delete in command prompt to change font color)
            if sys.platform.startswith('win'):
                 print('Bards response: ', response)
            else:
                # Prints Bard response in red for linux & mac terminal
                print("\033[31m" + 'Bards response: ', response, '\n' + "\033[0m")
            speak(response)
            
if __name__ == '__main__':
    main()
