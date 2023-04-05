velocidade = int(input('Velocidade: '))
limit = 80
if velocidade <= limit:
    print('Dentro do limite, você não foi multado! ')
else:
    multa = (velocidade - limit) * 7
    print(f'Você foi multado no valor de: R$ {multa}.00')
