number = input("Digite um número inteiro: ")

try:
    number = int(number)
except:
    print('Erro! Esse número não é inteiro.')
    exit()

if number % 2 == 0:
    print(f'{number} número é par!')
else:
    print(f'{number} número é impar!')
  