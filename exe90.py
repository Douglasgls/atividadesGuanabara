boletim = {}
nome = input('nome: ')
media = float(input(f'media de {nome}: ' ))
boletim['aluno'] = nome
boletim['media'] = media
if media >= 7:
    situação = 'Aprovado'
else:
    situação = 'Reprovado'
boletim['situação'] = situação
print(f'O nome é igual a ', nome)
print(f'a media de {nome} é {media}')
print(f'a situação de {nome} é {situação}')