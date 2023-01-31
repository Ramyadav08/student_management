import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os

def sptext():
    reconizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing..........")
        reconizer.adjust_for_ambient_noise(source)
        audio=reconizer.listen(source)
        try:
            print("reconizing.........")
            data=reconizer.recognize_google(audio)
            return  data
        except sr.UnknownValueError:
            print("please tell me again")
def txtsp(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    while True:
        data1=sptext().lower()
        if " what is your name " in data1:
            name="my name is Ab devilliers"
            txtsp(name)
        elif "old are you " in data1:
            old="i am 1 years old"
            txtsp(old)
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I:%M:%p")
            txtsp(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "facebook"in data1:
            webbrowser.open("https://www.facebook.com/")
        elif "play song" in data1:
            add="E:\Music"
            listsong=os.listdir(add)
            print("listsong")
            os.startfile(os.path.join(add,listsong[0]))
        elif "exit"in data1:
            txtsp("thank you")
            break

