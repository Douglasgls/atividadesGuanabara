op = "S"

m = 0
f = 0

cont_idade = 0
cont_mul20 = 0 
while op == "S":
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()
    if idade > 18 and sexo == "M":
        cont_idade += 1
        m+=1
        op= str(input('Quer continuar? [S/N] ')).upper()
    elif idade <= 18 and sexo == "M":
        op= str(input('Quer continuar? [S/N] ')).upper()
    elif idade > 18 and sexo == "F":
        cont_idade += 1


    if idade < 20 and sexo == "F":
        f+=1
        op= str(input('Quer continuar? [S/N] ')).upper()
    elif idade >= 20 and sexo == "F":
        op= str(input('Quer continuar? [S/N] ')).upper()



print(f'Total de pessoas com mais de 18 ano {cont_idade}')
print(f'Ao todo temos {m} homens cadastrados ')
print(f'E temos {f} mulheres com menos de 20 anos')


