#Ejercicios extra de Iterables y Listas: PROGRAMA VALIDA EL VALOR MÁS PEQUEÑO
'''Cree un programa que muestre el valor más pequeño de una lista'''

print("---- Analiza Cuál es el Número menor de una Lista  ----")

#Declaración de Lista
my_list = [9, 4, 7, 1, 5]

#Declaración de Variables
smallest_number = int
smallest_number = 0


#Declaramos como menor el primer número y lo comparamos
smallest_number = my_list[0]

for index in range (0, len(my_list)):
    if smallest_number >  my_list[index]:
        smallest_number =  my_list[index]

print(f"El menor valor es {smallest_number}")
