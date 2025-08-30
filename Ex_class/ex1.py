import numpy as np

dataset = np.loadtxt("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv", delimiter = ";" , dtype= str, encoding = "utf-8")

coutry = dataset[0, : 4]

taxa_alfabetizacao = dataset[1:, 9].astype(float)

taxa_media = taxa_alfabetizacao.mean()


pais = dataset[:, 1]

quantidade_america = np.sum(np.char.find(pais, "NORTHERN AMERICA" )!= -1)


regiao = dataset[0: ,1]

unica_regiao = np.unique(regiao)






regiao_latam = np.where(regiao == "LATIN AMER. & CARIB    ")

rendas = dataset[0: ,9]
rendas_america = rendas[regiao_latam]
local = dataset[0:,0]
pais  = local[regiao_latam]
maior_reda_caribe = np.argmax(rendas_america)

print(coutry)

print("Unicas regioes:")

print(unica_regiao)

print(f" Taxa da media de alfabetizacao: {taxa_media}")

print (f" Quantidade de paises da amrica do norte: {quantidade_america}")

print(f"Pais com maior renda da america do sul e caribe: {pais[maior_reda_caribe]}")