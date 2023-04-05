frase = str(input('frase: ')).lower().replace(' ','')
As = frase.count('a')
print(As)

frase_fatiada = frase.find('a')+1
frase_fand = frase.rfind('a')+1
print(frase_fatiada)
print(frase_fand)