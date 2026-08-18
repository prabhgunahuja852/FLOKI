import pyttsx3
import speech_recognition as sr
import webbrowser
import sys
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    speak("Hello, I am Floki. How may I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except:
        print("Say that again please...")
        return "none"
    return query.lower()

def tell_day_time():
    now = datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%H:%M:%S")
    speak(f"Today is {day} and the current time is {time}")
    print(f"Today is {day} and the current time is {time}")

def google_search_and_read(query):
    speak(f"Searching Google for {query}")
    try:
        for url in search(query, num_results=1):
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all('p')
            text = ""
            for p in paragraphs:
                text += p.get_text() + " "
                if len(text.split()) > 80:  # read first ~80 words
                    break
            if text:
                print(f"Information from {url}:\n{text}")
                speak(text)
            else:
                speak("Sorry, I could not extract readable information from the page.")
            break
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, something went wrong while fetching information.")

if __name__ == "__main__":
    speak("Say Valhalla to wake me up.")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Waiting for wake word 'Valhalla'...")
            audio = r.listen(source)
        try:
            wake_word = r.recognize_google(audio, language='en-in').lower()
            print(f"You said: {wake_word}")
        except:
            continue

        if "valhalla" in wake_word:
            speak("Yes, my lord.")
            wish_me()
            while True:
                query = take_command()
                if query == "none":
                    continue
                if "open youtube" in query:
                    speak("Opening YouTube")
                    webbrowser.open("https://www.youtube.com")
                elif "open google" in query:
                    speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                elif "open gmail" in query:
                    speak("Opening Gmail")
                    webbrowser.open("https://mail.google.com")
                elif "open whatsapp" in query:
                    speak("Opening WhatsApp Web")
                    webbrowser.open("https://web.whatsapp.com")
                elif "what time is it" in query or "tell me the time" in query or "what day is it" in query:
                    tell_day_time()
                elif "exit" in query or "quit" in query or "stop" in query:
                    speak("Goodbye! Have a nice day.")
                    sys.exit()
                else:
                    google_search_and_read(query)
