ladoA = int(input('lado A: '))
ladoB = int(input('lado B: '))
ladoC = int(input('lado C: '))

if ladoA == ladoB and ladoB == ladoC:
    print('EQUILÁTERO')
elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
    print('ISÓCELES')
elif ladoA != ladoB or ladoA != ladoC or ladoB != ladoC:
    print('ESCALENO')