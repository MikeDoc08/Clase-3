# 2. Paso de argumentos por referencia (mutable):

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    print("Dentro de la función:", lista)

# Llamada a la función con una lista
mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 5)
print("Fuera de la función:", mi_lista)
