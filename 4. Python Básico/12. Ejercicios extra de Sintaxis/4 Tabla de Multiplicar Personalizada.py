#Ejercicios Extras de Sintaxis: 4 Tabla de Multiplicar Personalizada
'''Pida al usuario un número del 1 al 10
Muestre su tabla de multiplicar del 1 al 12'''

print ("---- Tabla de Multiplicar personalizada ----")

#Declaración de variables
#////////////////////////////////////////////////
user_number = int
result = int
user_number = 0
result = 0

#Pedir información a cliente
user_number = int(input("Ingrese un número: "))

#////////////////////////////////////////////////
#Proceso 
for multiplication in range(1,13):
    result  = user_number * multiplication
    print(f"{user_number} X {multiplication} = {result}")