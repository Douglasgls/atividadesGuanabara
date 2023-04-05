nome = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ctps = int(input('carteira de trabalho (0 não tem): '))
idade =  2023 - ano_nascimento

if ctps >= 1:
    contratação = int(input('Contratação: '))
    salario = float(input("Salario: "))
    contribuição = (contratação + 35 ) - 2023 + idade
dici = {
    'nome': nome , 'idade': idade , 'ctps' : ctps , 'aposentadoria' :  contribuição
}
print(dici)