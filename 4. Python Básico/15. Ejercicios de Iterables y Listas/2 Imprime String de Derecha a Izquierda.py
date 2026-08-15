#Ejercicios de Iterables y Listas: IMPRIME UN STRING LETRA POR LETRA DE DERECHA A IZQUIERDA
'''Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.'''

print("---- Imprime un string letra por letra de derecha a izquierda ----")

#  Declaración o creación de lista
my_string = "Pizza con piña"


for index in range (len(my_string)-1,-1,-1):
    print(my_string[index]) 