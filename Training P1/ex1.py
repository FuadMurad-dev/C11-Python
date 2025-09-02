import numpy as np

dataset = np.loadtxt("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv", delimiter=";" , dtype=str , encoding= "utf-8" )

regioes = dataset[1: ,1]

regioes_africa = np.char.find(regioes, "SUB-SAHARAN AFRICA") != -1

pt_africa = dataset[1:,2][regioes_africa].astype(float)

total = np.sum(pt_africa)

print(total)






