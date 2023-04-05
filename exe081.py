numeros = []
op = ''
while op != 'N':
    numeros.append(int(input('digite um num: ')))
    op = input('quer continuar [N/S]').upper()
novo = numeros
novo.sort()
novo.reverse()
print('tamanho da lista',len(novo))
print('lista decrecente: ',novo)
if 5 in numeros:
    inde = novo.index(5)
    print(f'o valor cinco esta ná posição {inde} ')