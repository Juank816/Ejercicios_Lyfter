# Ejercicios guiados en Python
'''Ejercicio:2 Simulador de Ahorro'''

print("---- Simulador de Ahorro ----")

#Declaración de variables
#////////////////////////////////////////////////
name = input("Ingrese su nombre: ")
monthly_savings = float(input("¿Cuántos dolares ahorras por mes? "))
months = int(input("¿Cuántos meses deseas simular? "))
total = 0

#Ciclo y sus instrucciones
#////////////////////////////////////////////////
for month in range (1, months+1):
    total = total + monthly_savings
    print(f"Mes {month}: total acumulado = {total}")
    
#Mostrar el resultado
#///////////////////////////////////////////////////
print(f"{name}, en {months} habrás ahorrado: {total}")
