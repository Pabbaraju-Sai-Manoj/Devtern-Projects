import speech_recognition as sr
import pyttsx3
import wikipedia

def initialize_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

engine = initialize_engine()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
    except sr.UnknownValueError:
        text = "Sorry, I did not get that"
    except sr.RequestError:
        text = "Sorry, the service is down"
    return text

def process_command(command):
    command = command.lower()
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'hello' in command:
        speak('Hello! How can I assist you?')
    elif 'your name' in command:
        speak('I am your Python voice assistant.')
    else:
        speak('Sorry, I did not understand that command.')

while True:
    command = recognize_speech()
    process_command(command)
