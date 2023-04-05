
sexo = str(input(('manda teu sexo: [M/F]'))).upper()
while sexo != 'M' and sexo != 'F':
    print('Dado Invalido...')
    sexo = str(input('tente novamente: ')).upper()
print(f'registrado com sucesso {sexo}')