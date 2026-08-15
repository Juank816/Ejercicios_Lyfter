#El ciclo while
counter = 1

# El ciclo se ejecutará mientras contador sea menor a 5
while counter <= 5:
    print(f"El contador va por {counter}")

    # Incrementamos el contador para que la condición eventualmente sea False
    counter += 1

print("¡El while ha terminado!")
# Otro ejemplo de while
favorite_word = input("Digite su palabra favorita: ")

# El ciclo continuará mientras lo que escribamos NO sea "salir"
while favorite_word != "salir":
    print(f"Su palabra favorita es '{favorite_word}'. ")
    favorite_word = input("Digite otra palabra favorita: ")

print("¡Sesión finalizada con éxito!")

#////////////////////////////////////////////////////////////////////////////////////////////
#El ciclo for
list_of_car_brands = ["Mercedes Benz", "Toyota", "Mazda", "Hyundai"]

# Por cada elemento en la lista, ejecutamos el bloque
for car_brand in list_of_car_brands:
    print(f"Ejecutando ciclo para marca: {car_brand}")

print("¡Ciclo completado!")

# Un ciclo for con la función range 
# range(5) genera números del 0 al 4 (5 números en total)
for number in range(5):
    print(f"Número: {number}")
#/////////////////////////////////////////////////////////////
#Comando break
# Recorremos del 1 al 9
for number in range(1, 10):
    if number == 4:
        print("Número 4 encontrado, deteniendo ciclo...")
         # Salimos del for completamente
        break
    print(f"Revisando número: {number}")
#/////////////////////////////////////////////////////////////
#Comando continue
# Recorremos del 1 al 4
for number in range(1, 5):
    if number == 3:
        print("Saltando el número 3...")
        continue # Ignora lo que sigue y va a la siguiente vuelta
    print(f"Imprimiendo número: {number}")