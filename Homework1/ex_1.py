
nome = input("Nome: ")

nome_ma = nome.upper()
nome_mi = nome.lower()
quantidade_letras = len(nome.replace(" ", ""))
nome_inatel = nome.replace("Murad", "Inatel").replace("murad", "Inatel")

print(f"Letras Maiusculas: {nome_ma}")
print(f"Letras Minusculas: {nome_mi}")


print(f"Quantidade de letras: {quantidade_letras}")


print(f"Ultimo nome inatel: {nome_inatel}")
