import pyttsx3
engine = pyttsx3.init('sapi5')
a = str (input ("Enter the term: "))
engine.say(a)
engine.runAndWait()