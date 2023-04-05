c = 0
numeros = []
op = ''
while op != 'N':
    n = int(input('digite um num: '))
    if c == 0:
        numeros.append(n)
        print('valor adicionado com sucesso...')
        op = str(input('quer continuar [S/N]')).upper()
    else:
        if n in numeros :
                print('Número já está na lista...')
                op = str(input('quer continuar [S/N]')).upper()
        else:
                numeros.append(n)
                print('valor adicionado com sucesso...')
                op = str(input('quer continuar [S/N]')).upper()

    c+=1
novo = numeros
novo.sort()
print(novo)
print(numeros.sort()) # retorna none descubra depois...
