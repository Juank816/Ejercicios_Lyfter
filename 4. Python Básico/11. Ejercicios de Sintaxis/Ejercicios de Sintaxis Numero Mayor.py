#Ejercicios de Sintaxis: NÚMERO MAYOR DE 3
'''Cree un programa que le pida tres números al usuario y muestre el mayor.'''

print ("---- Analiza de tres Números el Mayor ----")

#Declaración de variables
#////////////////////////////////////////////////
number1 = 0
number2= 0
number3 = 0
larger_number = 0

#Se le piden los datos al cliente 
number1 = int(input("Ingrese el primer número. "))
number2 = int(input("Ingrese el segundo número. "))
number3 = int(input("Ingrese el tercer número. ")) 


#Proceso condicionales
#////////////////////////////////////////////////
larger_number = number1
if number2 > larger_number:
    larger_number = number2
if number3 > larger_number:
    larger_number = number3

#Mostrar en pantalla
print(f"El número mayor es {larger_number}")
