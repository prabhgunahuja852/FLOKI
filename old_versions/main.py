import wikipedia
import webbrowser
import sys
from datetime import datetime


def speak(text):
    print(f"Floki: {text}")


def wish_me():
    speak("Hello, I am Floki. How may I help you today?")


def tell_day_time():
    now = datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%H:%M:%S")
    return f"Today is {day} and the current time is {time}"


def process_command(query):
    query = query.lower()

    if query == "none":
        return ""

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open gmail" in query:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp Web"

    elif "chatgpt" in query or "chat g p t" in query:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    elif (
        "what time is it" in query
        or "tell me the time" in query
        or "what day is it" in query
    ):
        return tell_day_time()

    elif "exit" in query or "quit" in query or "stop" in query:
        return "Goodbye! Have a nice day."

    else:
        try:
            results = wikipedia.summary(
                query,
                sentences=2,
                auto_suggest=True
            )

            return f"According to Wikipedia:\n{results}"

        except wikipedia.exceptions.DisambiguationError:
            return "This topic is ambiguous. Please be more specific."

        except wikipedia.exceptions.PageError:
            return "Sorry, I couldn't find any information on that topic."

        except Exception as e:
            return f"Sorry, something went wrong: {e}"


if __name__ == "__main__":
    wish_me()

    while True:
        query = input("You: ")

        response = process_command(query)

        if response:
            speak(response)

        if query.lower() in ["exit", "quit", "stop"]:
            sys.exit()