ano = int(input('Insira um ano: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('Ano bissexto')
    else:
        print('Ano NÂO BISSEXTO')
elif ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano Não BISSEXTO')