#Ejercicios extra de Iterables y Listas: PROGRAMA CUENTA CUANTAS VECES APARECE UN NÚMERO EN UNA LISTA
'''Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una 
lista de números y otro número a buscar'''

print("---- Cuenta Cuantas Veces Aparece un Número en una Lista  ----")

#Declaración de Lista
number_list = []

#Declaración de Variables
number = 0
number_counter = 0
number_search = 0

#Se le pide información al Usuario

for index in range(0, 7):
    number = int(input(f"ingrese el número #{index + 1} a la lista: "))
    number_list.append(number)



#Analiza que número se repite
number_searh = int(input(f"Ingrese el número a buscar: "))
for index in range(0, 7):
    if number_search == number_list[index]:
        number_counter += 1

#Muestra en Pantalla
print(f"El número {number_search} aparece {number_counter} veces.")

#NOTA DE CORRECCION: "En el código aparecen líneas como number = int, number_counter = int, number_searh = int.
# En Python, esto asigna el tipo int como valor a la variable, lo cual no es necesario. Para inicializar una 
# variable numérica en 0, basta con escribir directamente number = 0. Es un detalle que no afecta el 
# funcionamiento del programa, pero adoptar esta forma más limpia va a hacer el código más claro a medida que 
# los programas crezcan.
#También hay un pequeño typo en el nombre number_searh, que debería ser number_search. Nada grave, 
# pero los nombres precisos ayudan mucho cuando el código se vuelve más largo."

