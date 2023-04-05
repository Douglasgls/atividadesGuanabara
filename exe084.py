op = ''
c = 0
pessoas = []
while op != 'N':
    nome = str(input('nome: '))
    peso = float(input('peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    c+=1

    op = input('quer continuar [N/S]').upper()
t = 1
while t < len(pessoas):
    if pessoas[t] == maior:
        nome_P = pessoas[t-1]
    elif pessoas[t] == menor:
        nome_p = pessoas[t-1]
    t+=2

print(f'numero de pessoas cadastradas {len(pessoas)/2}')
print(f'maior peso foi de {maior}KG de {nome_P}')
print(f'O menor peso foi de {menor}KG de {nome_p}')