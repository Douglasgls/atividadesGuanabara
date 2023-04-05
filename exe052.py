c = 0
n = int(input('numero: '))
for i in range(1,n+1):
    if n % i  == 0:
        c += 1

print(f'o numero {n} foi divisivel {c}x')
if c > 2:
        print('è por isso ele não é primo')
else:
     print('è por isso ele  é primo')