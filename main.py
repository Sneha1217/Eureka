import pyttsx3 #pip install pyttsx3
#import SpeechRecognition as sr #pip install speechRecognition #pip install pypi (for audio)
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your assistant. Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('RakeshSingh22565@gmail.com', 'tommyhilfigher329jndwk')
    server.sendmail('RakeshSingh22565@gmail.com', to, content)
    server.close()

if __name__ == "__main__":

    i = 1
    if i == 1:

        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('C://Program Files//Google//Chrome//Application//chrome.exe'))

        wishMe()
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif ('open stackoverflow' in query) or ('open stack overflow' in query):
            webbrowser.get('chrome').open("stackoverflow.com")

        elif ('open geeks for geeks' in query) or ('open geeksforgeeks' in query):
            webbrowser.get('chrome').open("https://www.geeksforgeeks.org/")

        elif 'open amazon' in query:
            webbrowser.get('chrome').open("amazon.com")

        elif 'open news' in query:
            webbrowser.get('chrome').open("timesofindia.indiatimes.com")


        elif 'play music' in query:
            music_dir = 'C://Users//DELL//Desktop//Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"hello, the time is {strTime}")

        elif 'email to navi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "navineha2003@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend NAVI. I am not able to send this email")

        i = 0
