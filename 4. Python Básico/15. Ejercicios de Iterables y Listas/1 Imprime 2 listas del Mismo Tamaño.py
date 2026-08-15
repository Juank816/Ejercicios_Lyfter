#Ejercicios de Iterables y Listas: IMPRIME LOS VALORES DE DOS LISTAS DEL MISMO TAMAÑO
'''Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.'''

print("---- Imprime dos listas al mismo tiempo y del mismo tamaño ----")

#  Declaración o creación de listas
first_list = [
    'Hay',
    'en',
    'que',
    'iteración',
    'indices',
    'muy',
]

second_list = [
    'casos',
    'los',
    'la',
    'por',
    'es',
    'util',
]




for index1 in range (0, len(first_list)): #Al ser las listas del mismo tamaño se toma de referencia una 
    record = first_list[index1]
    record2 = second_list[index1]
    print(record, record2)
    





