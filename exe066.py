somar = 0
num = ''
cont = -1
while num != '999':
    num = str(input('digite um num: '))
    cont+=1
    if num != '999':
        n = int(num)
        somar+=n

print(f'a soma dos {cont} foi de {somar}')