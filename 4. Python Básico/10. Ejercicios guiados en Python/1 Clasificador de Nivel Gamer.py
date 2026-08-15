# Ejercicios guiados en Python
'''Ejercicio:1 Clasificador de Nivel Gamer'''

print("---- Clasificador de Nivel Gamer ----")

#Declaración de variables
#////////////////////////////////////////////////
name = input("Ingresa tu nombre: ")
hours = int(input("¿Cuántas horas llevas jugando?" ))
is_competitive = input("¿Juegas competitivo? (si/no)")

#Condicional
#////////////////////////////////////////////////
if hours < 10: 
    category = "Novato 🟢"
    message = "¡Bienvenido al mundo gammer!"
elif hours < 50:
    category = "Casual 🔵" 
    message = "Ya le estás agarrando el ritmo"
elif hours < 200:
    category = "Gamer 🟣"
    message = "Definitivamente sabes lo que haces"
elif hours >= 200 and is_competitive == "si":
    category = "Pro 🔴"
    message = "Eres una leyenda viviente"
else:
    category = "Gamer 🟣"
    message = "Tienes la experiencia, pero aún no entras al competitivo."

#Mostrar el resultado
#///////////////////////////////////////////////////
print(f"{name}, tu categoría es: {category}")
print(message)
