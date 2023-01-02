# Voice-Assistant-Project

Voice Assistant Project is a voice assistant similar to the comic book character Iron Man’s voice assistant named Jarvis. Or we should say that it is similar to Google Assistant or Amazon Alexa.

The project consists of two python files. One is the main.py which is the program to be executed, and func.py contains some of the functions of main.py.
Firstly, a speech recognition engine is initialized by using speech_recognition module.

The command function provides the functionality to recognize the voice input given by the user. 
The smtp_email function adds up the functionality to send a voice assisted email.
In the main script firstly pyttsx3 text-to-speech engine with sapi5 driver is initialized.
Speak function makes use of this engine.
Wishme function wishes the user based on the current system time.
The run function runs all the functionality of the assistant like opening a website over a default browser, sending an email, or searching about something over Wikipedia.
