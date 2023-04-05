cidade = str(input('cidade nome: '))
N_c = cidade.split() # quebro cada palavra em uma lista
verificador  = 'santos' in N_c[0] #  verifica se santos esta na lista posição [0]
print(verificador)