import speech_recognition as sr
import os
import sys
import webbrowser

def talk (words):
    print(words)
    os.system("say" + words)

talk ("Привет, спроси что-нибудь ")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не понял")
        zadanie = command()

        return zadanie

def makeSomething (zadanie):
    if "open website" in zadanie:
        talk ("Уже открываю")
        url= "https://itproger.com"
        webbrowser.open(url)
    elif "stop" in zadanie:
        talk ("Да, конечно, без проблем")
        sys.exit()
while True:
    makeSomething(command())




