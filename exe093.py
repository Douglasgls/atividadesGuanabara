nome = str(input('Nome: '))
partidas = int(input('partidas jogadas: '))
total = 0
gols = []
for i in range(partidas):
    gol = int(input(f'quantos gols na partida {i}? '))
    total +=gol
    gols.append(gol)
tabela = {'nome': nome , 'gols' : gols, 'total' : total}
print(f'o campo nome tem o valor  {tabela["nome"]}  ')
print(f'o campo gols tem o valor {tabela["gols"]}')
print(f'o campo total tem o valor {tabela["total"]}')
print(f'o jogador {tabela["nome"]} jogou {partidas} paartidas.')
i = 0
c = 0
while i <= len(tabela["gols"])-1:
    print(f'Na partida {i}, fez {tabela["gols"][c]}')
    i+=1
    c+=1
print(f'foi um total de {tabela["total"]} gols')