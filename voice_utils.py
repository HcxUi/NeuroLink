
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""
