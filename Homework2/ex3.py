
nome_aluno = input("Nome do aluno: ")
media = float(input('Media do auluno: '))

aluno = {'nome' : nome_aluno, 'media' : media}

media = aluno['media']
if media >= 50:
    print('AP')
    status = "AP"

else:
    print('RP')
    status = "RP"


aluno['status'] = status

print(aluno)

