def ola_mundo():
    return 'Hello World!'

def mestre(funcao):
    return funcao()

exc = mestre(ola_mundo)
print(exc)