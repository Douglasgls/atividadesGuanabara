numA = int(input('primeiro número: '))
numB = int(input('segundo número: '))

if numA > numB:
    print(f'Maior número: ',numA)
    print(f'Menor número: ',numB)
elif numA == numB:
    print('os dois são iguai ')
else:
    print(f'Maior número: ',numB)
    print(f'Menor número: ',numA)