perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b':'4', 'c':'5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2' : {
        'pergunta': 'Quanto é 5+5?',
        'respostas': {'a': '2', 'b':'5', 'c':'10'},
        'resposta_certa': 'c'
    }
}

respostas_certas = 0
for chave, valor in perguntas.items():
    print(f'{chave}: {valor["pergunta"]}')
    print('Respostas: ')
    for letra_opc, resposta_opc in valor["respostas"].items():
        print(f'[{letra_opc}] {resposta_opc}')
    
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == valor["resposta_certa"]:
        print()
        print('BOAA!!! Acertouuu')
        print()
        respostas_certas += 1
    else:
        print()
        print('PUTSSSS, você errou!')
        print()
    
quantidade_perguntas = len(perguntas)
porcent_acertos = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi: {porcent_acertos}')