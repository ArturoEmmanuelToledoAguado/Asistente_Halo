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

#Habla
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Escucha
def listen():
    try:
        with sr.Microphone() as source:#Usamos el microfono como fuente
            print("Escuchando...")
            voice = listener.listen(source)#Escucha
            rec = listener.recognize_google(voice)#Pasa a texto lo escuchado
            rec = rec.lower()
            if name in rec:
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'que' in rec or 'halo' in rec:
        talk('En el mundo real, Halo es el nombre de un videojuego creado por la empresa BUNGIE estudios y estrenado el '
             '15 de noviembre del 2001 con la primer entrega de la franquicia llamada Halo: Combat Evolved; En el Lore '
             'del juego, Halo es el nombre de un sistema de armamento neurofísico creado por la raza de los Forerunners '
             'cuyo objetivo es eliminar la amenaza Flood de la galaxia.')
    if

run()