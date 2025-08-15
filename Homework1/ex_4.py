distancia = int(input("Qual a distancia da viagem em km ? "))


if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Valor da passagem: {preco}")


