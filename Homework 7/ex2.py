import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/space.csv" , delimiter= ";")
eua = ds[ds["Location"].str.contains("USA")]

company_eua = eua["Company Name"].nunique()

china = ds[ds["Location"].str.contains("China")]

company_china = china["Company Name"].nunique() 

paises = ["USA", "China"]
valores = [company_eua, company_china]


plt.bar(paises, valores, color = ["blue", "red"])

plt.title("Nurero de Companias")
plt.legend()
plt.xlabel("Pais")
plt.ylabel("Empresas")
plt.show()

print(company_eua)
print(company_china)


