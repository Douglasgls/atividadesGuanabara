'''
# eu q fiz!!!
num = int(input("digite um num: "))

ac = 1

while num > 1:
    fat = num * (num-1)
    num = num -2
    ac *= fat
    fat = fat * (num-1)
print(ac)
'''

'''
#  peguei na net
num = int(input("digite um num: "))
fatorial = 1
while num > 1:
    fatorial = fatorial * num
    num = num - 1
print(fatorial)
'''

numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)