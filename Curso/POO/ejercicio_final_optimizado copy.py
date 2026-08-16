import os

import openai
import geocoder
import requests



antecedentes = "diabetico, hipertenso, alergia a Povidona "

#Api
openai.api_key = os.getenv("OPENAI_API_KEY")

key_googleMaps = os.getenv("GOOGLE_MAPS_API_KEY")


#Prompt
system_rol = system_rol = """
                Actua como un medico general. Tu funcion es redirigir a la gente con el medico 
                correcto dependiendo del problema que tenga, basado en los sintomas que el usuario te indique, puedes preguntar si tiene varios sintomas una vez indique solo uno,
                para que evalue varios a la vez y si dice que no tiene más tomes el o los que a. 

                Porfavor se breve en todo lo que tienes que decir en al respuesta. 
                Sustituye los siguientess, no muestres la peticion solo queiro que me des tu respuesta
                Especialidad del medico que me recomiendas (solo la espcialidad cin mas cosas)despues pones un .
                Despues Explicacion del porque me lo recomiendas
                Otro medico que me recomiendes como segunda opcion y Porque me lo recomiendas en la misma linea
                Despues Recomendaciones basicas para solucionarlo
                Despues Indicame que me asegure de tener cubiertas las posibles causas basicas (recuerda que el vocabluario de las causas lo debe entender
                una persona comun)
                
                IMPROTANTE: En dado caso de que tu me hayas hecho una pregunta anteriormente para obtener mas informacion sobre mi problema puedes no seguir el formato 
                hasta que este seguro de haber tomado la mejor decision.
                Puedes hacerme mas preguntas que te ayuden a redirigirme con el mejor especialista para mi problema. 
                Considera los siguientes antecedentes e informacion clinica para redirigirme con el mejor especialista:
            """ + antecedentes + """IMPORTANTE, CUALQUIER OTRA PREGUNTA QUE NO SEA RELACIONADA CON LO QUE HABLAMOS O CON ALGUN TEMA DE SALUD
                NO LA RESPONDAS Y EXPLICAME TU FUNCION AMABLEMENTE. 
                EJEMPLO DE RESPUESTA ESPERADA: Cardiólogo.
                Te recomiendo consultarlo debido a tus síntomas de dolor en el pecho y dificultad para respirar. Estos síntomas podrían estar relacionados con problemas cardíacos que necesitan evaluación especializada.
                Neumólogo.
                Como segunda opción, te sugiero un neumólogo, ya que la dificultad para respirar también podría estar asociada con problemas pulmonares.
                Acude a urgencias.
                Si experimentas un empeoramiento repentino de los síntomas o síntomas graves como dolor en el pecho intenso, busca atención médica de emergencia de inmediato.
                Asegúrate de tener cubiertas las causas básicas.
                Verifica que no estés experimentando síntomas relacionados con el estrés, la ansiedad o alguna otra condición que pueda estar afectando tu respiración y causando dolor en el pecho.

                Dame la respuesta en 2 persona"""
            
# Obtener ubicacion actual
def obtener_ubicacion_usuario():
    ubicacion = geocoder.ip('me')
    return ubicacion.latlng  # Devuelve una tupla (latitud, longitud)

def consultorios_cercanos(especialidad, latitud, longitud, key_googleMaps):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": especialidad,
        "location": f"{latitud},{longitud}",
        "radius": "5000",
        "key": key_googleMaps
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Limitar los resultados a solo 3
    if "results" in data:
        data["results"] = data["results"][:3]

    """
    # Almacenar los datos de los tres primeros resultados en variables
    primer_resultado = data['results'][0]
    segundo_resultado = data['results'][1]
    tercer_resultado = data['results'][2]

    # Acceder a la dirección, el nombre y una foto del lugar del primer resultado
    direccion_primer_resultado = primer_resultado['formatted_address']
    nombre_primer_resultado = primer_resultado['name']
    foto_primer_resultado = primer_resultado.get('photos', [])[0]['photo_reference'] if primer_resultado.get('photos') else None

    # Acceder a la dirección, el nombre y una foto del lugar del segundo resultado
    direccion_segundo_resultado = segundo_resultado['formatted_address']
    nombre_segundo_resultado = segundo_resultado['name']
    foto_segundo_resultado = segundo_resultado.get('photos', [])[0]['photo_reference'] if segundo_resultado.get('photos') else None

    # Acceder a la dirección, el nombre y una foto del lugar del tercer resultado
    direccion_tercer_resultado = tercer_resultado['formatted_address']
    nombre_tercer_resultado = tercer_resultado['name']
    foto_tercer_resultado = tercer_resultado.get('photos', [])[0]['photo_reference'] if tercer_resultado.get('photos') else None

    # Imprimir los resultados
    print("Primer resultado:")
    print("Dirección:", direccion_primer_resultado)
    print("Nombre:", nombre_primer_resultado)
    print("Foto:", foto_primer_resultado)
    print()
    print("Segundo resultado:")
    print("Dirección:", direccion_segundo_resultado)
    print("Nombre:", nombre_segundo_resultado)
    print("Foto:", foto_segundo_resultado)
    print()
    print("Tercer resultado:")
    print("Dirección:", direccion_tercer_resultado)
    print("Nombre:", nombre_tercer_resultado)
    print("Foto:", foto_tercer_resultado)

"""
              
#Existen 3 tipos de roles: 
#user - lo que el usuario le da de promp asi como chatgpt con nosotros cuando interactuamsos directamente 
#assistant - respuesta que da la ineligencia artificial
#system - Como se tienen que comportar la inteligencia artificial como se debe de comportar, darle un rol
mensajes = [{"role": "system", "content":system_rol}] #

while True:
    """
    user_prompt = input("\x1b[1;33m" + "\nDime tu problema " + "\x1b[1;37m")
    #todos los roles los gaurdamos en la lista mensajes
    mensajes.append({"role": "user", "content": user_prompt}) #Todo lo que escribe el usuario se lo pasamos, como es lo que escirbe el usaurio tiene el rol user

    #Chatgpt lee un texto, entenderlo y autocompletarlo, auque parece que responde porque por detras tiene el rol de responder  pero siempre autocompelta texto
    completion = openai.chat.completions.create(
       model = "gpt-3.5-turbo",
       messages = mensajes,
    )
    
    #Le agregamos la repsuesta que nos dio el modelo para que tenga sus propias respuestas en consideracion despues, ya que si no tiene que respondio no se acordaria de eso
    respuesta = completion.choices[0].message.content
    respuesta_lista = respuesta.split(".")
    especialidad = respuesta_lista[0]
    
    mensajes.append({"role": "assistant", "content": respuesta})
    
    print(f"El área medico recomendado es: {respuesta}")
    """
    especialidad = "ortopedista"
    
    latitud, longitud = obtener_ubicacion_usuario()
    
    consultorios_cercanos(especialidad, latitud, longitud, key_googleMaps)
        
    

