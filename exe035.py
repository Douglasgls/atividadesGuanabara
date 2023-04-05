ladoA = int(input('lado A: '))
ladoB = int(input('lado B: '))
ladoC = int(input('lado C: '))

if (ladoB + ladoC) > ladoA:
    print('Forma um triângulo')
elif(ladoA + ladoB) > ladoC:
        print('Forma um triângulo')
elif(ladoC + ladoA) > ladoB:
        print('Forma um triângulo')
else:
    print('Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: A soma de dois lados do trângulo tem que ser maior que a outra reta.')
