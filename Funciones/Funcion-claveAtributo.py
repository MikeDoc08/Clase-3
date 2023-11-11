# 6. Función con argumentos de palabra clave arbitrarios:

def imprimir_info(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

# Llamada a la función con argumentos de palabra clave
imprimir_info(nombre="Alice", edad=25, ciudad="Wonderland")

#  los dobles asteriscos ** antes del nombre de un parámetro indican 
# que la función puede recibir un número variable de argumentos de 
# palabras clave (keyword arguments). Este tipo de parámetro se llama 
# "desempaquetado de argumentos de palabras clave" y permite que la 
# función reciba cualquier cantidad de argumentos de palabras clave, 
# los cuales se agrupan en un diccionario.