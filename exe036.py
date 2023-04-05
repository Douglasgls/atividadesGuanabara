Valor_casa = int(input('Digite o valor da CASA: '))
salario = int(input('Digite o valor o seu SALARIO: '))
tempo = int(input('Digite o TEMPO de pagameto em ANOS: '))
tempo_meses = 12 * tempo

parcela = Valor_casa / tempo_meses

novo_salario = salario + (30/100 * salario)
if parcela > novo_salario:
    print('Financiamento NEGADO')
else:
    print('parabéns financiamento aprovado!')