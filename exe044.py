preco = float(input('Preço das compras: R$'))
print('Formas de Pagamento')
menu = input('[1] à vista dinheiro/cheque\n'
             '[2] à vista cartão\n'
             '[3] 2x no cartão\n'
             '[4] 3x ou mais no cartão\n'
             'Qual é a opção? ')

if menu == '1':
    dez_preco = 10/100 * preco
    novo_preco = preco - dez_preco
    print(f'Sua compra de {preco} vai custar R${novo_preco} no final')
elif menu  == '2':
    cinco_preco = 5/100 * preco
    novo_preco = preco - cinco_preco
    print(f'Sua compra de {preco} vai custar R${novo_preco} no final')
elif menu == '3':
    print(f'Vai custar R${preco}')
elif menu == '4':
    vezes = float(input('Quantas vezes? '))
    vinte_preco = 20/100 * preco
    preco_Juros = vinte_preco + preco
    res = preco_Juros / vezes
    print(f'Sua compra vai ser parcelada em {vezes}x de {res}0 COM JUROS')
    print(f'Sua compra de {preco} vai custar {preco_Juros}0 no final.')