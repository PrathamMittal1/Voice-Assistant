import datetime, wikipedia, webbrowser, pyttsx3
from func import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    t = datetime.datetime.now().hour
    greet = ''
    if 6 <= t < 12:
        greet = "Good Morning!"
    elif 12 <= t <= 16:
        greet = 'Good Afternoon!'
    elif 16 < t <= 21:
        greet = 'Good Evening!'
    else:
        greet = 'Hello!'
    print(f'{greet} I am Computer. How can I help you?')
    speak(f'{greet} I am Computer. How can I help you?')


def run():
    query = command().lower()
    if 'wikipedia' in query:
        print('Searching Wikipedia...')
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        wikipedia.set_lang('en')
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print("According to Wikipedia" + str(results))
        speak(results)
    elif 'open youtube' in query:
        print('Opening YouTube...')
        speak('Opening YouTube...')
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        print('Opening google.com...')
        speak('Opening google.com...')
        webbrowser.open("google.com")
    elif 'time' in query:
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is {t}")
        speak(f"The time is {t}")
    elif 'send email' in query:
        try:
            print('What should I say?')
            speak("What should I say?")
            content = command()
            to = "pratham9897521595@gmail.com"
            smtp_email(to, content)
            print('Email has been sent!')
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            print("Sorry my friend. I am not able to send mail. Try again later.")
            speak("Sorry my friend. I am not able to send mail. Try again later.")
    else:
        print('Couldn\'t recognize your voice. Please try again.')
        speak('Couldn\'t recognize your voice. Please try again.')


def main():
    print(header)
    while 1:
        mic = command().lower()
        if 'computer' in mic:
            wishme()
            run()


if __name__ == '__main__':
    main()
