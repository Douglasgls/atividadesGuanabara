media = 0 
somar = 0
contador = 0
op = ''
while op != "n":
    num = int(input('digite um num: '))
    somar = somar + num
    contador=contador+1
    media = somar/contador

    if contador == 1:
        maior = num 
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num

    
    op = str(input('continuar? s/n:  ')).lower()




print(f'media dos valores digitados {media}')
print(f'soma dos números {somar}')
print(f'contidade de números digitados {contador}')

print(f'maior {maior} e menor {menor}')