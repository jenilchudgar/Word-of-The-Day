import requests
import pyttsx3
from plyer import notification

URL = "https://random-words-api.vercel.app/word"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 140)
engine.setProperty('voices', voices[0])


def set_notification(title, msg, timeOut=10):
    notification.notify(
        title=title,
        message=msg,
        app_icon="icons/w.ico",
        timeout=timeOut
    )


def speak(audio: str):
    engine.say(audio)
    engine.runAndWait()


r = requests.get(url=URL)
data = r.json()

word = data[0]['word']
definition = data[0]['definition']
pronunciation = data[0]['pronunciation']
print(data)
speak(
    f"The word of the day is: {pronunciation}. I repeat {pronunciation}. It means {definition}")
speak("See Notification for more details...")
set_notification(title="Word of the Day",
                 msg=f"Word: {word}\nMeaning: {definition}\nPronuciation: {pronunciation}", timeOut=30)
