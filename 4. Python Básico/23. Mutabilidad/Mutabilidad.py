#TEMA: Mutabilidad 
# En Python, cada tipo de dato que usamos tiene una propiedad muy importante, para algunos podemos modificar
# su contenido después de ser creados, y otros deben permanecer fijos después de ser creados.
# A esta característica se le llama mutabilidad, y entenderla nos permite escribir código más predecible,
# más seguro y más eficiente.
# Pensemos en una construcción de LEGO. Empezamos con una base, vamos agregando piezas, 
# quitamos algunas, reemplazamos otras. La construcción que vemos al final no es la que teníamos al inicio,
# es el resultado de todas las decisiones que tomamos en el camino. El valor cambió, pero siempre fue la misma
# construcción en el mismo lugar.

'''MUTABLES'''
#LISTAS
tasks = ["buy groceries", "send email", "call doctor"]
print("Original:", tasks)

# Reemplazar un elemento
tasks[1] = "send report"
print("Despues de reemplazar:", tasks)

# Agregar un nuevo elemento
tasks.append("read book")
print("Despues de agregar:", tasks)

# Eliminar un elemento
tasks.remove("call doctor")
print("Despues de eliminar:", tasks)

#DICCIONARIOS
user = {"name": "Maria", "age": 28, "city": "Buenos Aires"}
print("Original:", user)

# Modificar un valor existente
user["age"] = 29
print("Despues de modificar:", user)

# Eliminar un par clave-valor
del user["city"]
print("Despues de eliminar:", user)


'''INMUTABLES'''
#TUPLAS
coordinates = (40.7128, -74.0060)  # Coordenadas de Nueva York
print("Coordenadas:", coordinates)

# Intentar modificar un valor genera un error
coordinates[0] = 0.0

#CADENAS DE TEXTO
greeting = "hello"
print("Original:", greeting)

# Para obtener una version modificada, creamos un string nuevo
capitalized = greeting.capitalize()
print("String nuevo:", capitalized)
print("Original sin cambios:", greeting)

# Intentar modificar un caracter genera un error
greeting[0] = "H"

#TIPOS DE DATOS BÁSICOS 
score = 100
print("ID antes:", id(score))  # Identificador del objeto en memoria

score = score + 10
print("ID despues:", id(score))  # Nuevo objeto, nuevo identificador
print("Valor:", score)