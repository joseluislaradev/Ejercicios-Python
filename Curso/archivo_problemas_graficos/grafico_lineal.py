import pandas as pd
import matplotlib.pyplot as plt #Es una libreria de visualizacion de datos de forma grafica, para instalar es: py -m pip install matplotlib
import seaborn as sns #Es una libreria de datos estadisticos, para instalar es: py -m pip install seaborn

df = pd.read_csv("archivo_problemas_graficos//pedos.csv")

sns.lineplot(x="fecha", y="pedos", data=df) #Crea el grafico y los datos donde se agarran

plt.plot("01-06", 17, "o") #Crea un puntito en el grafico en la posicion que pongamos, en mi caso en el mas alto
plt.show() #Muestra el grafico




