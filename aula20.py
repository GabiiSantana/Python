letraMaiuscula = input('Qual letra deseja deixar em maiúscula? ').lower()

texto = 'python é muito legal'
novaString = ''

for letra in texto:
	if letra == letraMaiuscula:
		letraMaiuscula = letraMaiuscula.upper()
		novaString += letraMaiuscula
	else:
		novaString += letra

print(novaString)