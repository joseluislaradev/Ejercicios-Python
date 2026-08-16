import pandas as pd
import matplotlib.pyplot as plt #Es una libreria de visualizacion de datos de forma grafica, para instalar es: py -m pip install matplotlib
import seaborn as sns #Es una libreria de datos estadisticos, para instalar es: py -m pip install seaborn

df = pd.read_csv("archivo_problemas_graficos//ingresos_personales.csv")

sns.barplot(x="fuente", y="ingresos", data=df) #Crea el grafico y los datos donde se agarran

total_ingresos = df["ingresos"].sum() #Suma todos lso elementos de la columna

plt.show() #Muestra el grafico
print(f"El total de ingresos es: {total_ingresos} USD")


