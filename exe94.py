op = ''
lista_dic = []
while op != "N":
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))
    creat = {'nome': nome , 'sexo': sexo ,'idade' :idade}
    lista_dic.append(creat)
    op = str(input('quer continuar [S/N] ? ')).upper()
print(f'O grupo tem {len(lista_dic)} pessoas')
soma = 0
c = 1
pessoas_acima_media = []
tamanho_lista = len(lista_dic)
for i in range(len(lista_dic)):
    idade = lista_dic[i]["idade"]
    soma+=idade
    media = soma/tamanho_lista
    if idade > media:
        pessoas_acima_media.append(creat["nome"])
for i in range(len(lista_dic)-1):
    if creat["sexo"] == 'F':
        print(f'As mulheres cadastradas foram {[creat["nome"]]}')

print(f'A media de idade é {media}.')
print(f'pessoas com idade acima da media {pessoas_acima_media}')
print(f'a media das idade é : ' ,media)

