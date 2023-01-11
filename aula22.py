digitado = ''
secreto = 'hackeado'
len_secreto = len(secreto) 
c = 0

while True:
    digitado = input('Digite uma letra para descobrir a palavra: ')
    if digitado in secreto:
        print(f'Acertou, {digitado}')
    