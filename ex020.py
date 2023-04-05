import random
from random import shuffle
# Embaralha os elementos de uma lista.
# esse shuffle é top


l1 = input(' nome aluno 1: ')
l2 = input(' nome aluno 2: ')
l3 = input(' nome aluno 3: ')
l4 = input(' nome aluno 4: ')

lista_alunos = [l1,l2,l3,l4]

random.shuffle(lista_alunos)
print(lista_alunos)