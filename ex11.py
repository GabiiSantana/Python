def mestre(funcao, *args, **kwargs): # Pegando os argumentos das funçoes
    return funcao(*args, **kwargs) # retornando eles

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

exc = mestre(fala_oi, 'Gabi') # chamei a funçao e o parâmetro
exc2 = mestre(saudacao, 'Olá', nome = 'Gabi') # chamei a funçao e os parâmetros
print(f'{exc} \n{exc2}')# Executei elas.