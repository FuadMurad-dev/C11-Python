  
#   Materia Tupla
tupla = ('Goku', 'Vegeta', 'Gohan', 'Trunks')
#Mostrando elementos 
print(tupla)


#SLICING DE ELEMENTOS

print(tupla[1:3]) 

print(tupla[2:1])

print(tupla[-2])

#funcao pre-prontas do python
print(len(tupla)) # len = lenf que vem de comprimento
print(max(tupla))
print(min(tupla))

#------------------------------------------------------------//-------------------------------------------------------------

# Materia Listas

lista = ['Goku', 'Vegeta', 'Gohan', 'Trunks']

print(lista)

#insetrindo elementos

lista.append('Bulma') # a funcao append ela coloca um elemento no final da lista 
lista.insert(1, 'Kuririn') # o inset é voce colocar um elemento na posicao que voce desejar. OBS: ELe nao sobreescreve o elemento

#ALterando elementos na lista

lista[0] = 'picolo'
print(lista) 

#Excluindo elementos

del lista[0] # removendo pela posicao
lista.remove('Bulma') # remocao pelo valor
print (lista)

#--------------------------------------------------------------//-------------------------------------------

#  Materia de Conjuntos (Sets)

conjunto = {'Goku', 'Vegeta', 'Gohan', 'Trunks'}
print (conjunto) 

# Adicionando elementos 

conjunto.add('Bulma') 
print(conjunto) 

#Excluindo elementos

conjunto.remove('Trunks') 

#---------------------------------------------------------//----------------------------------------------------------

# Materia de dicionario 

pessoal = {'nome' : 'Goku', 'Idade' : '43', 'Sexo' : 'masculino'}
print(pessoal) 

#Adicinando elementos

pessoal['race'] = 'sayajin'
pessoal['familia'] = ['gohan', 'goten', 'chichi', 'pan']

# Update
pessoal ['idade'] = 45
print (pessoal)

#Delete
del pessoal['Sexo']
print(pessoal)

print(pessoal['familia'[2]]) #acessando a CHICHI



