import numpy as np

dataset = np.loadtxt("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv", delimiter = ";" , dtype= str, encoding = "utf-8")

coutry = dataset[0:, 4]

print(coutry)

taxa_alfabetizacao = dataset[1:, 9]

taxa_alfabetizacao = taxa_alfabetizacao.astype(float)

taxa_media = taxa_alfabetizacao.mean()

print (taxa_media)

pais = dataset[:, 1]

quantidade_america = np.sum(np.char.find(pais, "NORTHERN AMERICA" )!= -1)

print (f" Quantidade de paises da amrica do norte: {quantidade_america}")

regiao = dataset[0: ,1]

unica_regiao = np.unique(regiao)

print(unica_regiao)


regiao_latam = np.where(regiao == "LATIN AMER. & CARIB    ")

rendas = dataset[0: ,9]
rendas_america = rendas[regiao_latam]
local = dataset[0:,0]
pais  = local[regiao_latam]
maior_reda_caribe = np.argmax(rendas_america)

print(f"Pais com maior renda da america do sul e caribe: {pais[maior_reda_caribe]}") 




