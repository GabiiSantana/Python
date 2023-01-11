nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
nome_space = ' ' in nome

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem espaços: {nome_space}')
    print(f'Essa é a primeira letra do seu nome: {nome[0]}')
    print(f'Essa é a últoma letra do seu nome: {nome[-1]}')
else:
    print('Você não digitou nada')