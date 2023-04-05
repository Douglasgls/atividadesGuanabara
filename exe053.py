frase = str(input('manda: ')).replace(' ','').upper()


inverso = ''
for i in range(len(frase)-1,-1,-1):
    inverso+=frase[i]
if frase == inverso:
    print('é palindromo')
else:
    print('Não é palindromo')
