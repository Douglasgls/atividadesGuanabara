notaA = float(input('Primeira Nota: '))
notaB = float(input('Segunda Nota: '))

media = (notaA + notaB) / 2 

if media >= 7:
    print('APROVADO')
elif media > 4 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')