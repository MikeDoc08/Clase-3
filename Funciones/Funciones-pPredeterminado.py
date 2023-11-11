# 4. Función con parámetros predeterminados:

def saludar_persona(nombre, saludo="Hola"):
    print("{} {}!".format(saludo, nombre))

# Llamada a la función con un solo argumento
saludar_persona("Alice")

# Llamada a la función con ambos argumentos
saludar_persona("Bob", "Saludos")
