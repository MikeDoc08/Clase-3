# 1. Suma de elementos en una lista
# Escribe una función que reciba una lista 
# de números y devuelva la suma de todos los 
# elementos.
array = [1, 2, 3, 4, 5]

def suma(lista):
    resultado = 0
    for elemento in lista:
        resultado += elemento
    print(resultado)

suma(array)
