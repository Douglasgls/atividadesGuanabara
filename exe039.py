D_nascimento = int(input('Digite seu ano de nascimento xxxx : '))
print('--Apenas números tá--')
idade = int(2023 - D_nascimento)

if idade == 18:
    print('É a hora de se alistar...')
elif idade < 18:
    print(f'ainda vai se alistar ao serviço militar, falta {18 - idade}.')
elif idade > 18:
    print(f'Passou do tempo de alistamento em {idade - 18} Anos.')