lista = [1, 2, 3, 2, 4, 5, 6, 10, 8, 9, 10]
set_lista = set()
duplicado = -1

for numero in lista:
    if numero in set_lista:
        duplicado = numero
        break
    set_lista.add(numero)
    
print(duplicado)
