import random
from random import randint


menu = input('[0] Pedra\n'
        '[1] Papel\n'
        '[2] Tesoura\n'
        'Qual é a opção? ')

menu_int = int(menu)
if menu_int < 0 or menu_int >2:
    print("INVALIDO")

pc = random.randint(0,2)

if menu == '0' and pc == 0:
    print(f'você escolheu PEDRA e a MAQUINA PEDRA')
    print('logo foi EMPATE')
elif menu == '0' and pc == 1:
    print(f'Você escolheu PEDRA e a MAQUINA PAPEL')
    print('A maquina ganhou ')
elif menu == '0' and pc == 2:
    print('você escolheu PEDRA e a MAQUINA tesoura')
    print('JOGADOR ganhou')

if menu == '1' and pc == 1:
    print('você escolheu PAPEL e a maquina PAPEL')
    print('logo foi EMPATE')
elif menu == '1' and pc == 2:
    print(f'Você escolheu PAPEL e a MAQUINA TESOURA')
    print('A maquina  GANHOU')
elif menu == '1' and pc == 0:
     print(f'Você escolheu PAPEL e a MAQUINA PEDRA')
     print('JOGADOR GANHOU')

if menu == '2' and pc == 0:
    print(f'Você escolheu TESOURA e a maquina PEDRA')
    print('MAQUINA GANHOU')
elif menu == '2' and pc == 1:
    print(f'Você escolheu TESOURA e a maquina PAPEL')
    print('JOGADOR GANHOU')
elif menu == '2' and pc == 2:
    print(f'Você escolheu TESOURA e a maquina TESOURA')
    print('logo foi EMPATE')