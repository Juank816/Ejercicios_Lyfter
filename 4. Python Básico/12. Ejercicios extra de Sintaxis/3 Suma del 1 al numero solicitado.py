#Ejercicios Extras de Sintaxis: CALCULAR SUMA DEL NUMERO SOLICITADO 1 AL #
'''Cree un programa que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta 
ese número ingresado. Luego muestre el resultado de la suma.”.'''

print ("---- Suma del 1 al Número Solicitado ----")


#Declaración de variables
#////////////////////////////////////////////////
user_number = int
addition = int
counter = int
user_number = 0
addition = 0
counter = 1

#Pedir información a cliente
user_number = int(input("Ingrese un número: "))

#Ciclo while
while counter <= user_number:
    addition = addition + counter
    counter += 1

#Muestra el resultado
print(f"El resultado de la suma es: {addition}")