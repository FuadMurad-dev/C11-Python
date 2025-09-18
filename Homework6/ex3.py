import pandas as pd
import numpy as np

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")


region = ds.groupby("Region")

literancy_mean = region["Literacy (%)"].mean()

print("Lista de todas as regioes com literancy")

print(f"{literancy_mean.round(2)}") # round 2 é pra mostrar so dois numeros depois da virgula
