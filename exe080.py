numeros = []
for i in range(1,6):
    n = int(input('digite um num: '))
    if i == 1 or n > numeros[-1]:
        numeros.append(n)
        print('adicionado no final na lista')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos,n)
                print(f'adicionado na lista posição {pos}')
                break
            pos+=1
print(numeros)
   