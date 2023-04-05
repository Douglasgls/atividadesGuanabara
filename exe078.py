# 20/02 2023
numeros = []
for i in range(1,6):
    n = int(input(f'digite um numero na {i}° posição:'))
    numeros.append(n)
    
    maior = max(numeros)
    menor = min(numeros)

    indexM = numeros.index(maior)
    indexm = numeros.index(menor)


print(f'o maior numero é {maior} ná posição {i}')

print(f'o menor numero é {menor} ná posição {indexm+1}')


'''
num = []
for i in range (5):
    num.append(int(input(f'digite um num: {i} ')))

    maior = max(num)
    menor = min(num)

for pos , k in enumerate(num):
        if k == maior:
            print(f'o maior número digitado foi {maior} na posição {pos}')

for pos, m in enumerate(num):
    if m == menor:
        print(f'menor número digitado foi: {menor} na posição {pos}')
'''
