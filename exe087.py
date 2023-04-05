c = 0
matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        n = int(input(f'digite o valor para {i} {j}: '))
        matriz[i].append(n)
va = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            va+=matriz[i][j]
c = -1
somac3 = 0
contador = 0
while contador <= 2:
    coluna_3 = matriz[c][-1]
    somac3+=coluna_3
    c+=1
    contador+=1

novo = max(matriz[1])
print('a soma dos valores pares é: ' ,va)
print('maior valor da tabela 2 é:' , novo)
print('a soma dos elementos da coluna 3 é: ',somac3)

