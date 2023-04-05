'''
listagem =('Pão', 3, 'cafe',7.50, 'guarana',6.80)
#print(f'{listagem[0]}..........R$ {listagem[1]}')
#print(f'{listagem[2]}..........R$ {listagem[3]}')
#print(f'{listagem[4]}..........R$ {listagem[5]}')

c = 0
j = 1
for i in listagem:
    print(f'{listagem[c]}..........R$ {listagem[j]}')
    c+=2
    j+=2
'''




'''
# jeito GUANABARA
listagem =('Pão', 3, 'cafe',7.50, 'guarana',6.80)

for i in range(0,len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]}',end='..........')
    else: 
        print(f'R${listagem[i]}')
'''
