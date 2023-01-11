from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -=1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)

print(novo_cpf)