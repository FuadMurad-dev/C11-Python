numero = int(input("Escolha um numero para a tabuada: "))
intervalo_inicio = int(input("Escolha o intervalo inicial desse numero: "))
intervalo_final = int(input("Escolha o intervalo final desse numero: "))

for i in range(intervalo_inicio, intervalo_final + 1):
    tabuada = numero * i 
    print(f"{numero} x {i} = {tabuada}")


