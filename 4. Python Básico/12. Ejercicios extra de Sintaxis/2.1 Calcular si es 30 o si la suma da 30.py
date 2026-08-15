#Ejercicios Extras de Sintaxis: 2.1 CALCULAR SI ES 30 O LA SUMA DA 30 
'''Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30,
mostrar “Correcto”. Sino, mostrar “incorrecto”.'''

print ("---- Analiza y valida si un número es 30 o la suma da 30 ----")


#Declaración de variables
#////////////////////////////////////////////////
number1  = int
number2 = int
number3 = int
addition = int
number1 = 0 
number2= 0 
number3 = 0
addition = 0

#Pedir información a cliente
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

#Proceso
addition = number1 + number2 +number3

#Condición 
if addition == 30 or number1 == 30 or number2 == 30 or number3 == 30:
    print("Correcto")
else:
    print("Incorrecto")