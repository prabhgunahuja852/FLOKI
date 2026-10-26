
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import json
import urllib.request
from datetime import datetime


# AWS API Gateway endpoint
API_URL = "https://qpu8w7bxn9.execute-api.ap-southeast-2.amazonaws.com/status"


def speak(text):
    """Speak a response and print it in the terminal."""
    print(f"Floki: {text}")

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")

    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()


def wish_me():
    speak("Hello, I am Floki. How may I help you today?")


def take_command():
    """Listen to the microphone and convert speech into text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )
        print(f"You said: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return "none"

    except sr.RequestError:
        speak("Speech recognition is currently unavailable.")
        return "none"


def tell_day_time():
    """Return the current day and time."""
    now = datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%H:%M:%S")

    return f"Today is {day} and the current time is {time}"


def check_cloud_status():
    """Contact AWS API Gateway and retrieve the Lambda response."""
    try:
        request = urllib.request.Request(
            API_URL,
            headers={"Accept": "application/json"},
            method="GET"
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data.get("status") == "online":
            return data.get(
                "message",
                "Floki cloud connection successful!"
            )

        return "AWS responded, but the cloud status was unexpected."

    except Exception as error:
        print(f"AWS connection error: {error}")
        return (
            "I couldn't connect to the Floki cloud service. "
            "Please check your internet connection."
        )


def process_command(query):
    """Process recognised voice commands."""
    query = query.lower().strip()

    if query == "none":
        return

    elif any(phrase in query for phrase in [
        "check cloud status",
        "cloud status",
        "check aws",
        "check cloud connection",
        "test cloud connection"
    ]):
        speak("Checking Floki's cloud connection.")
        response = check_cloud_status()
        speak(response)

    elif "open youtube" in query:
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

    elif "chatgpt" in query or "chat g p t" in query:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif (
        "what time is it" in query
        or "tell me the time" in query
        or "what day is it" in query
    ):
        speak(tell_day_time())

    elif "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye! Have a nice day.")
        sys.exit()

    else:
        speak("Searching Wikipedia...")

        try:
            results = wikipedia.summary(
                query,
                sentences=2,
                auto_suggest=True
            )

            speak("According to Wikipedia")
            print(results)
            speak(results)

        except wikipedia.exceptions.DisambiguationError:
            speak("This topic is ambiguous. Please be more specific.")

        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on that topic.")

        except Exception as error:
            print(f"Wikipedia error: {error}")
            speak("Sorry, something went wrong while searching Wikipedia.")


if __name__ == "__main__":
    speak("Say Valhalla to wake me up.")

    while True:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Waiting for wake word 'Valhalla'...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            wake_word = recognizer.recognize_google(
                audio,
                language="en-in"
            ).lower()

            print(f"You said: {wake_word}")

        except sr.UnknownValueError:
            continue

        except sr.RequestError:
            print("Speech recognition service unavailable.")
            continue

        if "valhalla" in wake_word:
            speak("Yes, my lord.")
            wish_me()

            while True:
                query = take_command()

                if query == "none":
                    continue

                if any(word in query for word in [
                    "exit",
                    "quit",
                    "stop"
                ]):
                    speak("Goodbye! Have a nice day.")
                    sys.exit()

                process_command(query)
