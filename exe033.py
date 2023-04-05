num1 = int(input('num 1: '))
num2 = int(input('num 2: '))
num3 = int(input('num 3: '))

if num1 > num2 and num1> num3:
    maior = num1
    if num2 > num3:
        menor = num3
    else:
        menor = num2
    print(f'maior {maior} e o menor {menor}')
if num2 > num1 and num2 > num3:
    maior = num2
    if num1> num3:
        menor = num3
    else:
        menor = num1
    print(f'maior {maior}, menor {menor}')
if num3 > num1 and num3 > num2:
    maior = num3
    if num2 > num1:
        menor = num1
    else:
        menor = num2
    print(f'maior {maior}, e  menor {menor}')