"""Este codigo viola varios principios SOLID,
el primero porque la clase Analizador de sentimientos naliza el sentimiento y ademas formatea la cadena de 
salida indicando que cmabie de color y luego regrese a blanco.

El segundo principio tambien porque si queremos agregar mas rangos de polaridad tendriamos que modifciar
la clase y deberia poderse exterder de otra manera

el tercero no aplcia, porque no hay herencia

el cuearto tampoco aplica

el quinto si, porque la calse en lugar de depender de openai directamente deberia depender de una abstraccion"""

import os

import openai

#Api
openai.api_key = os.getenv("OPENAI_API_KEY")

#Prompt
system_rol = """Haz de cuenta que eres una analizador de sentimientos. 
                Yo te paso mensajes y tu analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres.
                SOLO RESPUESTAS NUMERICAS, donde -1 es negatividad maxima, 0 es neutral
                y 1 es positividad maxima. Puedes ir entre esos rangos, es decir 0.3, -0.5 y todos los
                decimales entre los rango son tambien validos (Solo puedes responder con ints o floats)"""
              
#Existen 3 tipos de roles: 
#user - lo que el usuario le da de promp asi como chatgpt con nosotros cuando interactuamsos directamente 
#assistant - respuesta que da la ineligencia artificial
#system - Como se tienen que comportar la inteligencia artificial como se debe de comportar, darle un rol
mensajes = [{"role": "system", "content":system_rol}] #

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if  -0.6 <= polaridad < -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[1;37m" #Le da un color a la respuesta en la consola
        elif -0.3 <= polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[1;37m"
        elif -0.1 <= polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[1;37m" 
        elif 0.1 <= polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[1;37m" 
        elif 0.4 <= polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[1;37m" 
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo" + "\x1b[1;37m" 
        else: 
            return "\x1b[1;31m" + "Muy negativo" + "\x1b[1;37m" 
  
analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime algo para analizar: " + "\x1b[1;37m")
    #todos los roles los gaurdamos en la lista mensajes
    mensajes.append({"role": "user", "content": user_prompt}) #Todo lo que escribe el usuario se lo pasamos, como es lo que escirbe el usaurio tiene el rol user

    #Chatgpt lee un texto, entenderlo y autocompletarlo, auque parece que responde porque por detras tiene el rol de responder  pero siempre autocompelta texto
    completion = openai.chat.completions.create(
       model = "gpt-3.5-turbo",
       messages = mensajes,
       max_tokens = 6 
    )
    
    #Le agregamos la repsuesta que nos dio el modelo para que tenga sus propias respuestas en consideracion despues, ya que si no tiene que respondio no se acordaria de eso
    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta)) #La respuesta de chatgpt siempre es str por eso la transformamos
    
    print(sentimiento)


