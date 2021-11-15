import speech_recognition as sr#Reconoce la voz
import pyttsx3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

name = 'max'
listener = sr.Recognizer()
engine = pyttsx3.init()#Hablar

voices = engine.getProperty('voices')#Obtenenos la lista de voces
engine.setProperty('voice', voices[0].id)

#Saludo
engine.say("Hola soy max, un asistente virtual para la historia de halo.")
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
    if ('que es' in rec) or ('halo' in rec):
        talk('En el mundo real, Halo es el nombre de un videojuego creado por la empresa BUNGIE estudios y estrenado el '
             '15 de noviembre del 2001 con la primer entrega de la franquicia llamada Halo: Combat Evolved; En el Lore '
             'del juego, Halo es el nombre de un sistema de armamento neurofísico creado por la raza de los Forerunners '
             'cuyo objetivo es eliminar la amenaza Flood de la galaxia.')

    if ('sistema' in rec) or ('armamento' in rec) or ('armament' in rec):
        talk('Sistema que ataca al sistema nervioso de todas las criaturas conscientes en su rango de alcance')

    if ('representaban' in rec) or ('juego' in rec) or ('eran' in rec) or ('represent' in rec):
        talk('Mediante estructuras en forma de anillos de entre 10,000 a 30,000 kilometros de diametro que tenian el '
             'poder militar de acabar con la vida consciente en la galaxia')

    if ('Forerunners' in rec) or ('for runners' in rec):
        talk('Los Forerunner fueron una antigua civilización de habilidosos constructores, brillantes pensadores y '
             'audaces guerreros elevados por los Precursores para que les sirvieran como asistentes y ayudantes; '
             'Después de la desaparición de los Precursores, los Forerunner tomaron el Manto de Responsabilidad y '
             'sirvieron fielmente como mayordomos de toda la vida en la galaxia, aunque su ambición ocasionalmente '
             'excedió su juicio.')

    if ('que son' in rec) or ('precursores' in rec):
        talk('Es la primer civilizacion de la que se tienen registros en la vía láctea, creadores de otras razas '
             'conscientes')

    if ('como desaparecieron' in rec) or ('como desaparecer' in rec):
        talk('Los precursores no aprobaban la descarada forma en que los Forerunners se adjudicaron el manto de '
             'responsabilidad, así que decidieron eliminar a la raza forerunner y ceder el manto a otras especies que '
             'consideran dignas; cuando los Forerunners se enteraron de los planes de sus creadores decidieron '
             'atacarlos con una avanzada militar de proporciones nunca antes vistas')

    if ('manto' in rec) or ('responsabilidad' in rec) or ('responsability' in rec):
        talk('Filosofía de los precursores basada en la creencia de que la forma de vida consciente más avanzada debería'
             ' proteger a la galaxia y todos sus seres vivientes en la galaxia.')

    if ('lucien' in rec) and ('for runners' in rec):
        img = mpimg.imread('Frun.png')
        imgplot = plt.imshow(img)
        plt.show()
        talk('Los Forerunners estaban clasificados en cinco niveles: Minero: Expertos en las ingenierías planetarias y '
             'estelares, responsables de reunir recursos para los proyectos de construcción; '
             'Trabajador de vida: No tenían comparación en cuanto a sus conocimientos sobre biología y medicina, por lo '
             'que cuidaban e incluso creaban formas de vida. '
             'Guerrero-Sirviente: Rango que constituía el ancho de la milicia de los Forerunners; operaban las '
             'magníficas naves de batalla y máquinas de guerra.'
             'Prometeos: Eran la forma más elevada y evolucionada del rango Guerrero-Sirviente; considerados '
             'combatientes Forerruner de élite. '
             'Constructor: Eran el grado más alto dentro de la sociedad Forerunner, encargados de construir naves, '
             'armas y las megaestructuras')

    if ('muestrame' in rec) and ('lucien' in rec) or ('muscle' in rec):
        img = mpimg.imread('Pre.jpg')
        imgplot = plt.imshow(img)
        plt.show()

run()