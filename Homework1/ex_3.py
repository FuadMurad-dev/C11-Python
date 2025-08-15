
sexo = input("insira seu sexo: ")

while sexo != "m" and sexo != "f":
    print("sexo invalido, insira m ou f")
    sexo = input("insira seu sexo novamente: ")

if sexo == "m": 
    print("homem")
else:
    print("mulher")
