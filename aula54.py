def func(*args, **kwargs):
		print(args)
		idade = kwargs.get('nome')
		if idade is not None:
				print(idade)
		else:
				print('Valor inválido.')

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
#desempacotando uma lista
func(*lista, *lista2, sobrenome = 'Santana')