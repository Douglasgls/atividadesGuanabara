import random
from random import randint

numPC = random.randint(0,5)
chute = int(input('digite seu chute de 0 a 5: '))
if chute > 5 or chute < 0:
    print('entre 0 e 5')
elif numPC  == chute:
    print('PARABÉNS' )
else:
    print('LOSER')