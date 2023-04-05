op = "S"
somar = 0
mais_mil = 0
cont = 1
while op == "S":
    produto = str(input('nome do produto: '))
    preco = int(input('preço: '))

    somar+=preco

    if preco >= 1000:
        mais_mil+=1
    
    if cont == 1:
        barato = preco
    else:
        if barato > preco:
            barato = preco
            Nome_barato = produto
    cont+=1
    op = str(input('quer continuar [ s/n]: ')).upper()

print(f'O tota da compra foi de {somar}')
print(f'temos {mais_mil} custando mais de 1000')
print(f'o produto mais barato foi {Nome_barato} de {barato}')


    


