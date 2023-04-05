distancia  = int(input('Distancia da viagem Em KM: '))
if distancia <=200:
    passagem = distancia * 0.50
    print('R$',passagem)
elif distancia > 200:
    passagem =  distancia * 0.45
    print('R$',passagem)