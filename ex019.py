import random
from random import choice
# choice é para pegar um elemento da lista,blz?

l1 = input(' nome aluno 1: ')
l2 = input(' nome aluno 2: ')
l3 = input(' nome aluno 3: ')
l4 = input(' nome aluno 4: ')

lista_alunos = [l1,l2,l3,l4]

aluno = random.choice(lista_alunos)
print(aluno)