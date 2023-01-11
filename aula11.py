""" Operadores lógicos
and
or
not
in
not in
"""

from sys import exit as encerrando

usuario_logado = []
senha_logado = []
logando = str(input('Você deseja CADASTRAR uma conta? [S/N] ')).upper()

def entrar():
    print('\n')
    usuario_input = str(input('Digite seu usuário: '))
    senha_input = input('Digite sua senha: ')
    
    print('\n')
    if usuario_input in usuario_logado and  senha_input in senha_logado:
        print('Logando no sistema')
    elif usuario_input in usuario_logado and senha_input not in senha_logado:
        print('Senha incorreta.')
    elif usuario_input not in usuario_logado and senha_input in senha_logado:
        print('Usuário incorreto.')
    else:
        print('Usuário e senha inválidos.')

if 'S' in logando:
    print('\n')
    print('=' * 40)
    usuario_cadastro = str(input("Digite seu usuário: "))
    senha_cadastro = input("Digite sua senha: ")
    print('\n')
    
    usuario_logado.append(usuario_cadastro)
    senha_logado.append(senha_cadastro)

    logando_pt2 = str(input('Deseja entrar? [S/N] ')).upper()
    if 'S' in logando_pt2:
        entrar()
    else:
        print('Ok, fechando aplicativo.')
        encerrando()

if 'N' in logando:
    print('Ok, fechando aplicativo.')
    encerrando()