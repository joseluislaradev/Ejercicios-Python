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

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self) -> str:
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre) #Funcion que sustituye los valores en donde se encuentran las llaves

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
        
        
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
            return Sentimiento("Muy negativo", "31")

rangos = [
    ((-0.6,-0.3), Sentimiento("negativo", "31")),
    ((-0.3,-0.1), Sentimiento("Algo negativo", "31")),
    ((-0.1,-0.1), Sentimiento("Neutral", "33")),
    ((0.1,-0.4), Sentimiento("Algo positivo", "32")),
    ((0.4,0.9), Sentimiento("Positivo", "32")),
    ((0.9,1), Sentimiento("Muy positivo", "32")),
]
  
analizador = AnalizadorDeSentimientos(rangos)

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


