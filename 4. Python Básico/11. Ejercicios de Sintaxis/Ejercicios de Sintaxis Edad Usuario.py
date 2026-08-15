#Ejercicios de Sintaxis: EDAD USUARIO
'''Ejercicio:2 Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé,
niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.'''

print("---- Clasificador por Edad ----")

#Declaración de variables
#////////////////////////////////////////////////
name = input("Ingrese su nombre: ")
last_name = input("Ingrese apellido: ")
age = int(input("Ingrese su edad: "))

#PROCESO
#////////////////////////////////////////////////
if age <= 2:
    print(f"{name} {last_name} es un bebé.")
elif age > 2 and age <= 11:
    print(f"{name} {last_name} es un niño.")
elif age > 11 and age <= 13:
    print(f"{name} {last_name} es un preadolescente.")  
elif age > 13 and age <= 17:
    print(f"{name} {last_name} es un adolescente.") 
elif age > 17 and age <= 35:
    print(f"{name} {last_name} es un adulto joven.") 
elif age > 35 and age <= 64:
    print(f"{name} {last_name} es un adulto.")
else:
    print(f"{name} {last_name} es un adulto mayor.")    