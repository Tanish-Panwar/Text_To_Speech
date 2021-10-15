# TEXT TO SPEECH:
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = input('Enter text:  ')
text.lower()
speak(text)
