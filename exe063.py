termo = int(input('Quantos termos você quer mostar: '))

if termo == 1:
    print('0')
elif termo == 2 or termo == 3:
    print('1')

contador = 3
p = 0
s = 1

print('0->1->1',end='->')
while contador< termo:
    proxT = p + s
    p = s
    s = proxT
    proxT = p + s
    contador+=1
    print(proxT,end='->')
print('acabou')
