c = 1
numeros = [[],[]]
while c < 8:
    n = int(input('digite um número: '))
    if c ==1:
        if n % 2 == 0:
            numeros[0].insert(0,n)
        else:
            numeros[1].insert(0,n)
    else:
        if n % 2 == 0:
            numeros[0].insert(0,n)
        else:
            numeros[1].insert(0,n)
    c+=1
novo = numeros
novo[0].sort()
print('pares',novo[0])

new = numeros
new[1].sort()
print('impares',new[1])