import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")

# Extraindo o 6 maiores paises em area do mundo

ds_maiores_paises = ds.nlargest(6, "Area (sq. mi.)")

#print(ds_maiores_paises['Country'])

# traçar um scatter plot que ilustre o GDP per capita desses paises

#plt.scatter(ds_maiores_paises['Country'], ds_maiores_paises['GDP ($ per capita)'], s = 50) # grafico de dispersão

#plt.show()

ds_Maiores_GDP = ds.nlargest(5, 'GDP ($ per capita)')

print(ds_Maiores_GDP["Country"])

plt.bar(ds_Maiores_GDP["Country"], ds_Maiores_GDP["GDP ($ per capita)"]) # grafico de barra

#lt.show()

# Extraindo os paises que nao tem acesso

dsnocost = ds[ds["Coastline (coast/area ratio)"] == 0]

# Extraindo quantos paises que nao tem costa

quantidadenocost = len(dsnocost)
quantidadecost = len(ds) - quantidadenocost

#plt.pie([quantidadenocost, quantidadecost], labels= ["Paises sem costa", "Paises com costa"], autopct= "%1.1f%%") #grafico pizza com porcentagem

plt.show()

