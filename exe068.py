import random
from random import randint



perder = 0

cont_vencer = 0

result = 0


while perder <= 0:
    pc = random.randint(1,20)
    num = int(input('diga um valor: '))
    escolha = str(input('par ou impar: [P/I]: ')).upper()
    result = num + pc


    if result % 2 == 0 and escolha == 'P':
        print(f'você jogou {num} e o pc {pc}. TOTAL DEU {result} PAR ')
        print('você ganhou')
        print('vamos jogar novamente...')
        cont_vencer = cont_vencer + 1 
    elif result % 2 != 0 and escolha == 'I':
        print(f'você jogou {num} e o pc {pc}. TOTAL DEU {result} IMPAR ')
        print('você ganhou')
        print('vamos jogar novamente...')
        cont_vencer = cont_vencer + 1 


    if result % 2 == 0 and escolha == 'I':
        print(f'você jogou {num} e o pc {pc}. TOTAL DEU {result} PAR ')
        print('você perdeu')
        print(f'GAME OVER... você venceu {cont_vencer}')
        perder = perder + 1
        break
    elif result % 2 != 0 and escolha == 'P':
        print(f'você jogou {num} e o pc {pc}. TOTAL DEU {result} IMPAR ')
        print('voce perdeu')
        print(f'GAME OVER... você venceu {cont_vencer}')
        perder = perder + 1
        break
       

