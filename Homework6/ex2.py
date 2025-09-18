import pandas as pd
import numpy as np

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")


population = ds.loc[ds["Population"].idxmax()]

region_population_max  = population["Region"]

country_population_max = population["Country"]

print(f"Pais que tem o maior indice de populacao: {country_population_max}")

print()

print(f" Regiao que tem maior indice de populacao: {region_population_max}")