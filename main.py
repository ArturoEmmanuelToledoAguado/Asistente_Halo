import speech_recognition as sr#Reconoce la voz
import pyttsx3

name = 'rubicon'
listener = sr.Recognizer()
engine = pyttsx3.init()#Hablar

voices = engine.getProperty('voices')#Obtenenos la lista de voces
engine.setProperty('voice', voices[0].id)

#Saludo
engine.say("Hola soy rubicon, un asistente virtual para la historia de halo.")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:#Usamos el microfono como fuente
        print("Escuchando...")
        voice = listener.listen(source)#Escucha
        rec = listener.recognize_google(voice)#Pasa a texto lo escuchado
        rec = rec.lower()
        if name in rec:
            talk(rec)
except:
    pass