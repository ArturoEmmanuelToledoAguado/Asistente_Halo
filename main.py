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
        #Provar 2.3
    if ('amenaza' in rec) and ('flood' in rec):
        talk('Los primeros registros de Flood datan de cuando los humanos y los San´Shyuum (profetas) comenzaron a '
             'experimentar con mutaciones provocadas por un misterioso polvo desecado que encontraron en una nave que '
             'se estrelló en los límites de la galaxia; el Flood pronto evolucionó hasta convertirse en un poderoso e '
             'intrincado sistema de formas grotescas virtualmente imposibles de detener.')

    if ('esparcer' in rec) or ('flood' in rec):
        talk('El Flood era un diseño malicioso: nació en forma de esporas virulentas, aunque de apariencia inofensiva. '
             'Poco a poco, las esporas comenzaron a atacar a las especies conscientes apoderándose de sus mentes y '
             'cuerpos, transformándolos en criaturas espantosamente mal formadas, capaces de infectar a otros de manera '
             'directa.')

    if ('son' in rec) and ('profetas' in rec):
        talk('Los San´Shyuum, también conocidos coloquialmente como Profetas, fueron los principales arquitectos del '
             'Covenant. Por milenios, los San´Shyuum adoraron a los Forerunner como dioses, y la base de su devoción '
             'giraba en torno a su erróneo concepto de trascendencia que estaba conectado con la Matriz de Halo. Como '
             'líderes religiosos del Covenant, la actividad principal de los Profetas era localizar, estudiar e '
             'incorporar tecnología Forerunner para estudiarla y eventualmente iniciar el Gran Viaje')

    if ('muestrame' in rec) and ('lucien' in rec) or ('profetas' in rec):
        img = mpimg.imread('Pro.jpg')
        imgplot = plt.imshow(img)
        plt.show()

    if ('muestrame' in rec) and ('espora' in rec):
        img = mpimg.imread('esp.jpg')
        imgplot = plt.imshow(img)
        plt.show()

    if ('muestrame' in rec) and ('humano' in rec):
        img = mpimg.imread('hum.jpg')
        imgplot = plt.imshow(img)
        plt.show()

    if ('partes' in rec) and ('historia' in rec) or ('history' in rec):
        talk('La mayoría de mis registros son de las siguientes periodos: El legado forerunner, Ascenso de la humanidad,'
             ' Fin de la guerra, Secuelas, Regreso de los prometeos')

    if ('legado' in rec) and ('for runner' in rec):
        talk('Periodo de tiempo que data desde el año 10,000,000 Antes de la Era Común al año 852 de la Era Común')

    if ('ascenso' in rec) and ('humanidad' in rec):
        talk('Periodo de tiempo que data desde el año 2080  de la Era Común al 2552 de la Era Común')

    if ('fin' in rec) or ('guerra' in rec):
        talk('Periodo de tiempo que data del año 2552  de la Era Común')

    if ('secuelas' in rec) or ('second' in rec):
        talk('Periodo de tiempo que data desde el año 2553  de la Era Común al 2556 de la Era Común')

    if ('regreso' in rec):
        talk('Periodo de tiempo que data desde el año 2557  de la Era Común al 2558 de la Era Común')
#3
    if ('creador' in rec) and ('intelectual' in rec):
        talk('Las personas a cargo de la primer entrega fueron Marcus R.Lehto que fue el director de arte creativo y '
             'Joseph Staten que fue el director y escritor.')
#4
    if ('entregas' in rec):
        talk('La fraquincia ha generado hasta ahorita 17 juegos y se esperan mas en un futuro.')

    if ('mas vendido' in rec):
        talk('El juego mas vendido de la franquicia fue Halo 5:Guardians')

    if ('menos vendido' in rec):
        talk('El juego menos vendido de la franquicia fue Halo: Fireteam Raven')

    if ('mas odiado' in rec):
        talk('El juego mas odiado fue Halo 5: Forge')

    if ('mejores criticas' in rec):
        talk('El juego con mejores reseñas es el Halo 3: ODST')

    if ('mas tiempo' in rec):
        talk('El juego mas largo en desarrollar es Halo Infinite')
#5
    if ('libros' in rec) or ('novelas' in rec):
        talk('Hasta el momento son 30 Libros.')

run()