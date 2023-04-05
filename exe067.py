condição = 1
tabu = 1
while tabu > 0:
    tabu =int(input("digite para ver sua tabuada: "))
    if tabu > 0:
        while  condição <= 10:
            print(f'{tabu} X {condição} = {tabu*condição}')
            condição = condição + 1
        condição = 1
    else:
        break


