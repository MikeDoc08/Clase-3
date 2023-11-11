# 5. Función con argumentos arbitrarios:

def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

# Llamada a la función con varios argumentos
imprimir_argumentos("uno", 2, [3, 4], "cinco")

args = ["uno", 2, [3, 4], "cinco"]


# El asterisco * antes del nombre de un parámetro indica que la función 
# puede recibir un número variable de argumentos posicionales. Este tipo 
# de parámetro se llama "empaquetado" o "empaquetado de argumentos" y 
# permite que la función reciba cualquier cantidad de argumentos posicionales, 
# los cuales se agrupan en una tupla.