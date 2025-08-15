import math

numero = float(input("Entre com um numero decimal: "))

raiz = numero ** (1/2)

print(f"Raiz quadrada do numero: {raiz}")

teto = math.ceil(numero)

print(f"Funcao teto: {teto}")

chao = math.floor(numero)

print(f"Funcao chao: {chao}")

print(f"parte inteira: {int(numero)}")
