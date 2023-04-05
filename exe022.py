Nome = str(input('Digite seu nome? '))
NoMe = Nome.upper() # letra maiuscula
nome = Nome.lower() # letra minuscula
nomeC = nome.strip() # letra  sem espaços
print(NoMe)
print(nome)
print(len(nomeC))
Nome_fatido = nome.split() # cada palavra vira uma letra 
print(len(Nome_fatido[0]))