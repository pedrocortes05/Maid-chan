import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices') #details of current voice
engine.setProperty('voices', voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def command(ask = False):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        if ask:
            print(ask)
            speak(ask)
        print("Listening...")
        r.pause_threshhold = 1
        audio = r.listen(source)
        voice_data = ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down")
        speak("Sorry, my speech service is down")
        return "None"
    return query

if __name__=="__main__":
    greetings()
    speak("Hello Pedro")
    
    while True:
        query = command().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'search' in query:
            search = command("What do you want to search for?")
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak("Here is what i found for " + search)
        
        if 'exit' in query:
            exit()
    
