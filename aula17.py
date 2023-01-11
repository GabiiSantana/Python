while True:
	num1 = input('Digite um número: ') 
	num2 = input('Digite outro número: ')
	opr = input('Digite um operador [+, -, /, *]: ')

	if not num1.isnumeric() or not num2.isnumeric():
		print('Por favor, digite um número!')
		break
	
	num1 = int(num1)
	num2 = int(num2)

	if opr == '+':
		print(f'{num1} + {num2} = {num1 + num2}')
		break
	elif opr == '-':
		print(f'{num1} - {num2} = {num1 - num2}')
		break
	elif opr == '/':
		print(f'{num1} / {num2} = {num1 / num2}')
		break
	elif opr == '*':
		print(f'{num1} * {num2} = {num1 * num2}')
		break
	else:
		print('error')
		break