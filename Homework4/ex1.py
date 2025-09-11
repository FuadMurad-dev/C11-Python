import numpy as np

dataset = np.loadtxt("C:/Users/murad/OneDrive/Documentos/C11-Python/space.csv", delimiter= ";", dtype= str, encoding= "utf-8")

porcentagem_success = dataset[dataset[:,7] == "Success"] # pega a quantidade de vezes que as missoes teve success 

porcentagem_media = len(porcentagem_success) / len(dataset) * 100 # faz a media das missoes que teve success em relacao ao total

custo_missao = dataset[1:,6] # pega os custos das missoes
custo_missao = custo_missao.astype(float) # passa de string para float

verifica_custo = custo_missao[custo_missao > 0].mean() # verifica se o custo > 0 e tira a media

missao_eua= dataset[:, 2] # pega a coluna das missoes no dataset
dataset_eua = np.sum(np.char.find(missao_eua , "USA") != -1) # pega a quantidade de vezes que o USA apareceu

empresa_spacex = dataset[dataset[:,1] == "SpaceX"]

missao_cara = empresa_spacex[:, 6] 
missao_cara = missao_cara.astype(float).argmax()

empresas , quantidade = np.unique(dataset[:,1], return_counts= True)

print(f"Porcentagem de sucesso nas missoes: {porcentagem_media:.2f}%") #:.2 é deixar duas casas decimais depis da virgula

print(f"Media dos custos das missoes: {verifica_custo:.2f}")

print(f" Quantidade de missoes que tem USA: {dataset_eua}")

print(f"Missao mais cara: {missao_cara}")

print("Nome das empresas e quantidade de missoes: \n") 

for i, j in zip(empresas, quantidade): 
    print(f"{i} : {j}")








