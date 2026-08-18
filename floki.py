import wikipedia
import webbrowser
import sys
from datetime import datetime


def speak(text):
    print(f"Floki: {text}")


def wish_me():
    speak("Hello, I am Floki. How may I help you today?")


def take_command():
    query = input("You: ")
    return query.lower()


def tell_day_time():
    now = datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%H:%M:%S")
    speak(f"Today is {day} and the current time is {time}")


if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        if query == "none":
            continue

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
            tell_day_time()

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            sys.exit()

        else:
            speak("Searching Wikipedia...")

            try:
                results = wikipedia.summary(query, sentences=2, auto_suggest=True)
                speak("According to Wikipedia")
                print(results)

            except wikipedia.exceptions.DisambiguationError:
                speak("This topic is ambiguous. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")

            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, something went wrong.")