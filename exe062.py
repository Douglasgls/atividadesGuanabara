P_termo = int(input('Primeiro termo: '))
razão = int(input('razão: '))


c = 1
n = 10
while c < n:
    pa = P_termo + razão
    P_termo = pa
    print(pa,end='->')
    c+=1
    print(end='')
    if c >= n:
        print()
        menu = int(input('quer ver mais quantos termos? '))
        if menu == 0:
            print('acabou')
        elif menu > 0:
            c = 0
            n = 0
            n+=menu 
        

