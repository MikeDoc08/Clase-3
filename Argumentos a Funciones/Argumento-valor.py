# 1. Paso de argumentos por valor (por defecto en Python):

def duplicar_numero(numero):
    numero *= 2
    print("Dentro de la función:", numero)

# Llamada a la función con un argumento
mi_numero = int(input('ingrese un numero'))


duplicar_numero(mi_numero)
print("Fuera de la función:", mi_numero)
