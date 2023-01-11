hora = input('Que horas são ai? [00:00] ')

try:
    hora = int(hora)
except:
    print('A hora deve ser um número inteiro.')
    exit()

if hora >= 0 and hora <= 11:
    print('Então bom dia!')
elif hora >= 12 and hora <= 17:
    print('Então boa tarde!')
elif hora >= 18 and hora <= 23:
    print('Então boa noite!')
else:
    print('Erro!')