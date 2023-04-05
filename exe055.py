peso = float(input(f'peso da 1° pessoa: '))
maior = peso
menor = peso
for i in range(2,6):
   pesofor = float(input(f'peso da {i}° pessoa: '))
   if pesofor > maior :
      maior = pesofor
   elif pesofor < menor:
      menor = pesofor





print('maior',maior)
print('menor', menor)