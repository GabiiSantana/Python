cpf_novo = '168995350'
cpf = '16899535009'
number = 10
number2 = 11
cpf_len = len(cpf)

while number != 1:
    soma = 0
    for numero in cpf_novo:
        numero = int(numero)
        mult = numero * number

        print(f'{numero} x {number} = {mult}')

        soma += mult
        number -= 1 

result = cpf_len - (soma % cpf_len)
if result > 9:
    result = 0

cpf_teste = cpf_novo + str(result)

####################################################################################

while number2 != 1:
    soma2 = 0
    for numero in cpf_teste:
        numero = int(numero)
        mult = numero * number2

        print(f'{numero} x {number2} = {mult}')

        soma2 += mult
        number2 -= 1 

result2 = cpf_len - (soma2 % cpf_len)
if result2 > 9:
    result2 = 0

cpf_teste = cpf_teste + str(result2)
print(cpf_teste)

if cpf_teste == cpf:
    print('CPF VÁLIDO!')
else:
    print('CPF INVÁLIDO!')