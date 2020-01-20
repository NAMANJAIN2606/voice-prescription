import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING!")

    speak("I AM Dr.MIC")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)

    except:
        #print(e)
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'name' in query:
            while True:

                r1= sr.Recognizer()
                with sr.Microphone() as source1:
                    print("say the name")
                    r1.pause_threshold = 1
                    audio1 = r1.listen(source1)

                try:
                    print("recognizing the name")
                    text1 = r1.recognize_google(audio1)
                    print('NAME  :   {}'.format(text1))
                    speak('name is {}'.format(text1))
                    break
                except:
                    #print(e)
                    print("Say that again")

        elif 'symptoms' in query:
            while True:
                r2= sr.Recognizer()
                with sr.Microphone() as source2:
                    print("say the symptoms")
                    r2.pause_threshold = 1
                    audio2 = r2.listen(source2)

                try:
                    print("recognizing the symptoms")
                    text2 = r2.recognize_google(audio2)
                    print('SYMPTOMS  :  {}'.format(text2))
                    speak('symptoms are {}'.format(text2))
                    break
                except:
                #print(e)
                    print("Say that again")

        elif 'prescription' in query:
            while True:
                r3= sr.Recognizer()
                with sr.Microphone() as source3:
                    print("say the prescription")
                    r3.pause_threshold = 2
                    audio3 = r3.listen(source3)

                try:
                    print("recognizing the prescription")
                    text3 = r3.recognize_google(audio3)
                    print('PRESCRIPTION  :  {}'.format(text3))
                    speak('prescription is {}'.format(text3))
                    break
                except:
                    #print(e)
                    print("Say that again")
            
        elif 'diagnosis' in query:
            while True:
                r4= sr.Recognizer()
                with sr.Microphone() as source4:
                    print("say the diagnosis")
                    r4.pause_threshold = 2
                    audio4 = r4.listen(source4)

                try:
                    print("recognizing the diagnosis")
                    text4 = r4.recognize_google(audio4)
                    print('DIAGNOSIS  :  {}'.format(text4))
                    speak('diagnosis required {}'.format(text4))
                    break
                except:
                #print(e)
                    print("Say that again")
            
        elif 'advice' in query:
            while True:
                r5= sr.Recognizer()
                with sr.Microphone() as source5:
                    print("say the advice")
                    r5.pause_threshold = 1
                    audio5 = r5.listen(source5)

                try:
                    print("recognizing the advice")
                    text5 = r5.recognize_google(audio5)
                    print('ADVICE  :  {}'.format(text5))
                    speak('advice is {}'.format(text5))
                    break
                except:
                #print(e)
                    print("Say that again")
            
        elif 'quit' in query:
            exit(0)

