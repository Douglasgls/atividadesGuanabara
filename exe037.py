
num = int(input('digite um número: '))
print('1-BINARIO\n2-octal\n3-hexadecimal')
menu = input('digite aqui:  ')

cociente = 1 
lista = []
if menu == '1':
    while cociente >=1:
        resto = num % 2
        lista.insert(0,resto)
        cociente = num // 2 
        num = cociente
    print (lista)
if menu == '2':
  print(oct(num))
if menu == '3':
   print(hex(num))

