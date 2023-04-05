P_termo = int(input('primeiro TERMO: '))
razao = int(input('razão: '))
decimo = P_termo + (10-1) * razao
for i in range(P_termo,decimo+1,razao):
    print(f'{i}',end='-> ')
print(end='acabou')