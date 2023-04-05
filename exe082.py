numeros = []
op = ''
while op != 'N':
    numeros.append(int(input('digite um num: ')))
    op = input('quer continuar [N/S]').upper()
par = []
impar = []
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])


print(f"Números digitados...{numeros}" )

print(f'Números pares...{par}')

print(f'Números impares...{impar} ')
