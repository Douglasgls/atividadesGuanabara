tab = (	
'América-MG',
	
'Athletico-PR',

'Atlético-MG',
	
'Bahia',
	
'Botafogo',

'Bragantino',
	
'Corinthians',
	
'Coritiba',

'Cruzeiro',
	
'Cuiabá',

'Flamengo',
	
'Fluminense',

'Fortaleza',
	
'Goiás',

'Grêmio',
	
'Internacional',
	
'Palmeiras',
	
'Santos',

'São Paulo',
	
'Vasco'
)

print('primeiros cincos são', tab[0:5])

print('os ultimos quatros são', tab[-4:])

print(sorted(tab))

index = tab.index('Palmeiras')
print(f'o palmeiras esta na posição {index}')