numero = int(input("Escolha um numero de 1000 ate 9999: "))


if  numero >= 1000 and numero <= 9999:
    print(f"numero da unidade: {numero}")

    dezena = numero // 10 

    print(f"numero da dezena: {dezena}")

    centena = numero //100 

    print(f"numero da centena: {centena}")

    milhar = numero// 1000

    print(f"numero do milhar : {milhar}")

else:
    print("numero fora do escopo pedido")





