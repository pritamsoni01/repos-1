import pyttsx3
import datetime
import speech_recognition as sr
import sys
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
     
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back pritam boss!")
    speak("Pritam boss the current time is")
    time()
    speak("Pritam boss the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning pritam boss")
    elif hour>=12 and hour<17:
        speak("Good afternoon pritam boss")
    elif hour>=17 and hour<24:
        speak("Happy and Energetic  evening pritam boss")
 
    else:
        speak("Good night pritam boss and have Sweet Dreams. ")
    speak("i am your personal AI assistant prem,   please tell me how can i help you?")
    

wishme()
exit()
