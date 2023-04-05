
id = 0
muie = 0
for i in range(1,5):
    print(f'---{i}° pessoa ---')
    nome = str(input('digite seu nome: '))
    idade = float(input('digite sua idade: '))
    sexo = str(input('digite seu sexo: M or F: ')).upper()

    id += idade
    media = id/4


    if i == 1:
        maior = 0
    if idade > maior:
            maior = idade
    if sexo == 'M' and idade == maior:
        nome_maior = nome
        idade_maior = maior


    if sexo == 'F' and idade < 20:
         muie +=1
print('')


print(f'A média das idades é {media}')
print(f'O homem mais velho tem {idade_maior} e se chama {nome_maior}')
print(f'Ao todo são {muie} mulheres menores de 20 anos')
