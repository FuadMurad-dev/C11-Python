
pessoas = []


for i in range (3):
    nome = input(f"Nome da pessoa {i+1}: ")
    peso = float(input(f"Peso da pessoa {i+1}: "))

    pessoas.append({'nome' : nome, 'peso' : peso})


    peso_max = max(k['peso'] for k in pessoas)
    peso_min = min(k['peso'] for k in pessoas)

for k in pessoas:
    if k['peso'] == peso_max:
        peso_max = k
    if k['peso'] == peso_min:
        peso_min = k
        
print(f"Pessoa mais pesada: {peso_max['nome']}")
print(f"Pessoa mais leve: {peso_min['nome']}" )