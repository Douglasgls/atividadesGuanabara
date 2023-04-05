import random
from random import randint
n = int(input('palpites: '))
for i in range(n):
    jogo = []
    c = 0
    while c < 6:
        sort = random.randint(1,60)
        if sort not in jogo:
            jogo.append(sort)
            c+=1
    print(f'jogo {i+1}°',sorted(jogo))















'''
qtd = int(input('Quantos jogos? '))
jogos = [[0, 0, 0, 0, 0, 0] for i in range(qtd)]
print(f'SORTEANDO {qtd} JOGOS...')
for i in range(qtd):
    pos = 0
    while pos < 6:
        rand = randint(1, 60)
        if rand not in jogos[i]:
            jogos[i][pos] = rand
            pos += 1
    print(f'Jogo {i+1}: {sorted(jogos[i])}')
'''
