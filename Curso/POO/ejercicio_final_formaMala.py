"""Desarrollar un chatbot en python que nos pida algo y tome eso que le decimos, analice el sentimiento
y nos responda cual es el sentimiento. """

from textblob import TextBlob #Para instalar es pip install textblob Es una liberia que analiza el lenguaje natural y te muestra su sentimiento, pero solo esta en ingles y no es precisa

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0: #La libreria arroja valores entre -1 y 1, siendo -1 el estado mas malo y uno uno bueno
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("Hola me quiero matar")
print(resultado)