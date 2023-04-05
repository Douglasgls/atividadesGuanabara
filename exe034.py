salaraio = int(input('lança teu salairo: '))
dez_salario  = 10/100 * salaraio
quinze_salario = 15/100 * salaraio
if salaraio > 1250:
    reajuste = salaraio + dez_salario
    print(f'Seu novo salario com aumento de 10% é: {reajuste}')
elif salaraio <= 1250:
    reajuste = salaraio + quinze_salario
    print(f'Seu novo salario com aumento de 15% é: {reajuste}')