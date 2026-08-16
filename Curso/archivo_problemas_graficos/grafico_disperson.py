import pandas as pd
import matplotlib.pyplot as plt #Es una libreria de visualizacion de datos de forma grafica, para instalar es: py -m pip install matplotlib
import seaborn as sns #Es una libreria de datos estadisticos, para instalar es: py -m pip install seaborn

df = pd.read_csv("archivo_problemas_graficos//bigotes.csv")

sns.boxplot(x="categoria", y="valor", data=df) #Crea el grafico y los datos donde se agarran

plt.show() #Muestra el grafico
