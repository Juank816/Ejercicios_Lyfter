#Ejercicios Extras de Sintaxis: CALCULAR MENOR O MAYOR A 10 MINUTOS
'''Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.
Si es exactamente igual, muestre “Igual”.'''


print ("---- Calcula TIEMPO MENOR O MAYOR A 10 MINUTOS ----")


#Declaración de variables
#////////////////////////////////////////////////
time_in_seconds = int
remaining_seconds = int
time_in_seconds = 0 
remaining_seconds = 0

#Pedir información a cliente
time_in_seconds = int(input("Ingrese un tiempo en segundos: "))

#Proceso (condición)
if time_in_seconds < 600:
    print("Es menor a 10 minutos.")
    remaining_seconds = 600 - time_in_seconds
    print(f"Faltarían {remaining_seconds} para llegar a 10 minutos.")
elif time_in_seconds == 600:
    print("Igual.")
else:
    print("Mayor.")


