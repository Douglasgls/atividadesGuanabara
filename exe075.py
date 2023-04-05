tupla = (int(input('digite um num: ')),int(input('digite um num: ')),int(input('digite um num: ')),int(input('digite um num: ')))

c = 0
for i in tupla:
    if i == 9:
        c+=1
    if i == 3:
        tres = tupla.index(3)
        print(f'o valor 3 apareceu na {tres+1}')
    if i % 2 == 0:
        print(f'os valores pares foram {i}')
print(f'o valor 9 apareceu {c}x ')
