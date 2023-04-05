peso = float(input('peso: '))
altura = float(input('altura: '))

icm = (peso / (altura**2))

if icm < 18.5:
    print('abaixo do peso')
elif icm >= 18.5 and icm  <= 25:
    print('peso ideal')
elif icm > 25 and icm <= 30:
    print('Sobrepeso')
elif icm > 30 and icm < 40:
    print('Obesidade')
elif icm > 40: 
    print('Obesidade morbida')