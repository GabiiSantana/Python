secreto = 'beautiful'
lista = []
chances = 3

while True:
    letra = input('\n Digite UMA letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
     
    lista.append(letra)

    if letra in secreto:
        print('Acertou uma letra \n')
    else:
        print('errou, tenta de novo! \n')
        lista.pop()

    temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in lista:
            temporario += letra_secreta
        else:
            temporario += '*'
    
    if letra not in secreto:
        chances -= 1
        print(f'Você só tem {chances} chances')
    if letra in secreto:
        print(f'Você tem {chances} chances')
    if chances == 0:
        print('Você perdeeeeu!')
        break
    
    if temporario == secreto:
        print(f"Você ganhou!!! A palavra era {secreto}")
        break
    else:
        print(f'A palavra está assim: {temporario}')