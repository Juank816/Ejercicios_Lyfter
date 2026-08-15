#Ejercicios de Iterables y Listas: INTERCAMBIA EL PIRMER Y ÚLTIMO NÚMERO DE UNA LISTA
'''Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.'''
print("---- Intercambia primer y último elemento de una lista ----")


#Declaración de variables
position1 = 0
final_position = 0
total_positions = 0


#Declaración de lista
my_list = [4, 3, 6, 1, 7]

#Se validan las posiciones
total_positions = len(my_list)
position1 = my_list[0]
final_position = my_list[total_positions-1]

#Asignar los valores nuevamente
my_list[0] = final_position
my_list[total_positions-1] = position1

'''#Eliminación de datos
my_list.pop(total_positions-1)
my_list.pop(0)'''

#Intercambio de posiciones        # /Lo que está comentado fue como se hizo incialmente, se corrige de una mane
#más fácil y clara según lo recomendado

#NOTA DE CORRECCIÓN "El resultado es correcto, pero el enfoque con pop() e insert() agrega pasos innecesarios.
# Una forma más directa sería guardar los valores en variables temporales y reasignarlos directamente 
# por índice, algo como: guardar el primero, guardar el último, y luego asignar cada uno en 
# la posición del otro. Esto hace el código más claro y fácil de leer."

'''my_list.insert(0, final_position)
my_list.insert(len(my_list),position1)'''

#Imprime en pantalla el resultado
for index in range (0, len(my_list)):
    print(my_list[index]) 
