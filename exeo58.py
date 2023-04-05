import random
from random import randint

pc = random.randint(0,5)
c = 0 

chute = int(input('digite um num 0 a 5: '))
while chute != pc:
    print('ERROU')
    chute = int(input('tente novamente: '))
    c+=1
print('ACERTOU...')
print(f'Número de Tentativas {c+1}')