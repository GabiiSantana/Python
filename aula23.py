variavel = ['Gabi', 'Nick', 'Maria']
comeca_com_g = False

for valor in variavel:
	if valor.startswith('G'):
		comeca_com_g = True

if comeca_com_g:
	print("Existe 'G' no nome.")
else:
	print("Não existe um nome que começa com 'G'")