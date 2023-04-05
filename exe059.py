v1 = int(input("valor 1: "))
v2 = int(input("valor 2: "))

opçao = 0
while opçao != 5:
    print('[1] somar\n'
          '[2] Multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa')
    menu = int(input('insira a opção: '))
    opçao = menu
    if menu == 1:
        print('SOMAR')
        print(f'soma de {v1} e {v2} = {v1+v2} ')
    elif menu == 2:
        print('MULTIPLICAR')
        print(f'a multiplição de {v1} e {v2} = {v1*v2}')
    elif menu == 3: 
        print('MAIOR')
        if v1 > v2:
            print(f'maior é {v1}')
        else:
            print(f'maior é {v2}')
    elif menu == 4:
        v1 = int(input("valor 1: "))
        v2 = int(input("valor 2: "))
    else:
        print("INSIRA UM NUM VÁLIDO")

