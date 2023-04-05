valor= int(input('digite um num para saque: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced+=1
    else:
        if totced > 0 :
            print(f'total de {totced} de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            break
        totced = 0