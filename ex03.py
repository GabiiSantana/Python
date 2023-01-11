nome = input('Digite seu nome: ')
lenNome = len(nome)

if nome.isnumeric():
    print('[ERRO] Seu nome contém números?')

if nome.isalpha():
    if lenNome <= 4:
        print('Seu nome é curto!')
    elif lenNome == 5 or lenNome == 6:
        print('Seu nome é normal!')
    elif lenNome > 6:
        print('Seu nome é muito grande!')
    else:
        print('ERRO!')