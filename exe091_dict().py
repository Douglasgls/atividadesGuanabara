import random
from random import randint

jogadores1 = random.randint(1,6)
jogadores2 = random.randint(1,6)
jogadores3 = random.randint(1,6)
jogadores4 = random.randint(1,6)
jogadores5 = random.randint(1,6)

jogo = {}

jogo['jogador1'] = jogadores1
jogo['jogador2'] = jogadores2
jogo['jogador3'] = jogadores3
jogo['jogador4'] = jogadores4
jogo['jogador5'] = jogadores5

#for k, v in sorted(jogo.items(), key=lambda item: item[1]):
    #print(k,v)
c = 1
for chave , valor in sorted(jogo.items(), key= lambda item: item[1], reverse=True):
    print(f'{c}° Lugar: {chave} {valor} ')
    c+=1


