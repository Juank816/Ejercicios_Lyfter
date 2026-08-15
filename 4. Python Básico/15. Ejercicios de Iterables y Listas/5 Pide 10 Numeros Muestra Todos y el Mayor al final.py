#Ejercicios de Iterables y Listas: PROGRAMA QUE ELIMINA TODOS LOS NÚMEROS IMPARES DE UNA LISTA
'''Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que 
ingresó, seguido del numero ingresado más alto.'''



print("---- Pide 10 números y los muestra todos, verificando cuál es el mayor  ----")

#Declaración de lista
my_list = [] 

#Declaración de variables
largest_number = int
number = int
largest_number = 0 
number = 0

#Pedirle información al usuario
for index in range(0,10):
    number = int(input(f"ingrese el número #{index + 1} a la lista: "))
    my_list.append(number)


#Analiza que número es el mayor
largest_number = my_list[0]
for index in range(0, len(my_list)):
    if my_list[index] > largest_number:
        largest_number = my_list[index] 

#Muestra la lista
for index in range(0, len(my_list)):
    print(my_list[index])

#Muestra el resultado
print(f"El número más alto fue: {largest_number}")