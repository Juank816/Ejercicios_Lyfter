#Ejercicios extra de Iterables y Listas: PROGRAMA CALCULA EL PROMEDIO DE LOS VALORES
'''Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree 
una nueva lista con solo los valores mayores al promedio'''

print("---- Calcula los el Promedio de los Valores y Muetra la lista de los Valores Mayores al Promedio  ----")

#Declaración de la lista
my_list = [10, 20, 30, 40, 50]
new_list = []

#Declaración de Variables
average = float
addition = float
average = 0
addition = 0

#Primero se hace la suma de las notas de la lista
for index in range(0,len(my_list)):
    addition += my_list[index]

#Proceso para Averiguar el Promedio 
average = addition / len(my_list)
print(f" El promedio es: {average}")

#Proceso para validar los Valores Mayores al prmedio
for index in range(0, len(my_list)):
    if my_list[index] > average:
        new_list.append(my_list[index])

#Muestra la nueva lista
print(new_list)