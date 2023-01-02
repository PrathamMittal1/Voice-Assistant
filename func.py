import smtplib
import speech_recognition as sr

password = ' xxxxx '
header = '''Computer Voice Assistant
 version 1, author: Pratham Mittal.
 
 Say \"Computer\" to wake me up.'''


def command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en_in')
        print(f'User said: {query}')
    except Exception as e:
        print(e, '\nCouldn\'t recognize, please try again.')
        return 'None'
    return str(query)


def smtp_email(to, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('12001151@csepup.ac.in', password)
    server.sendmail('12001151@csepup.ac.in', to, body)
    server.close()
