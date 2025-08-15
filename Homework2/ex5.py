
n = int(input('Quantidae de pessoas: '))

soma_idade = 0
contador = 0
for i in range (n):
    pessoas = {'nome': input(f"nome da pessoa {i + 1}: ") , 'idade' : int(input(f"Idade da pessoa {i + 1}: ")) , 'sexo' : input(f"Sexo da pessoa {i+ 1}: ")}
    pessoas[n] = pessoas
    soma_idade = soma_idade + pessoas['idade']
    if pessoas['idade'] < 20:
        contador = contador + 1
    
media = soma_idade/n

print(media)
print(contador)

