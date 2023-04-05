maior = 0
menor = 0
for i in range(1,8):
    idade = int(input(f'Ano de nascimento da {i}° pessoa: '))
    if idade > 2023:
        print('vai nascer ainda ? ')
        break
    idade = 2023 - idade 
    if idade >= 21:
        maior+=1
    if idade <= 21:
        menor+= 1
print(f'{maior} são menores de idade.')
print(f'{menor} são maiores de idade.')
    