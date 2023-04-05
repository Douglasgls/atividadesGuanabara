op = ''
boletim = []
while op != 'N':
    nome = [str(input('nome: '))]
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) /2
    boletim.append([nome,[nota1,nota2], media])
    op = input('quer continuar? [S/N]: ').upper()
for i in range(len(boletim)):
    print(f'NO: {i}---- Nome: {boletim[i][0]} --- Média: {boletim[i][2]}')

op = ''
while op != '999':
    n = int(input('mostrar nota de qual aluno:' ))
    for i in range(len(boletim)):
        print(boletim[n][1])
    op = str(input('quer continuar: 999; '))