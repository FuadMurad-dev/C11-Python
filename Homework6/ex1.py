import pandas as pd
import numpy as np

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")
#1)

#a)
regiaons_oceania = ds[ds["Region"].str.contains("OCEANIA")]

country_oceania = regiaons_oceania["Country"]

print("Paises que tem a regiao oceania: ")

print()

print(country_oceania)

#b)

country_oceania_sum = regiaons_oceania.shape[0]

print("Quantidade de paises que contem oceania")

print(country_oceania_sum)