#Ejercicios Extras de Sintaxis: 3.1 CALCULAR TEMPERATURAS CELSIUS A FAHRENHEIT Y KELVIN
'''Convertidor de unidades de temperatura
Pida al usuario ingresar una temperatura en Celsius
Conviértala a Fahrenheit y Kelvin
Muestre los tres valores'''

print ("---- Convertidor de Temperatura ----")

#Declaración de variables
#////////////////////////////////////////////////
degrees_celsius = float
degrees_fahrenheit = float
degrees_kelvin = float
degrees_celsius = 0
degrees_fahrenheit =  0 
degrees_kelvin = 0 

#Pedir información a cliente
degrees_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

#Proceso
degrees_fahrenheit = (degrees_celsius * 9 / 5) + 32
degrees_kelvin = degrees_celsius + 273.15

#Mostrar en Pantalla 
print(f"Fahrenheit: {degrees_fahrenheit}")
print(f"Kelvin: {degrees_kelvin}")