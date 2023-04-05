P_termo = int(input('Primeiro termo: '))
razão = int(input('razão: '))





c = 1
while c < 10:
    pa = P_termo + razão
    P_termo = pa
    print(pa,end='->')
    c+=1
print('Acabou')
