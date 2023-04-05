n = str(input('digite a expressão: '))
parentese = []

for i in range(0,len(n)):
    parentese.append(n[i])
    print(n[i])
if parentese.count('(') == parentese.count(')'):
    print("expressão valída")
else:
    print("A expressão não é valida")


'''
for c in range(0, len(txt)):
    exp.append(txt[c])
if exp.count('(') == exp.count(')'):
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
'''