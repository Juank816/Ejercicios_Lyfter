#Ejercicios de Diccionarios: DICCIONARIO CON DOS LISTAS DEL MISMO TAMAÑO
'''Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la 
otra para sus values.'''

print("---- Programa de Dos Listas una para sus Keys y otra para sus Values  ----")

#Declaramos las listas 
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

#Declaramos el diccionario que guarda la información solicita 
information_dictionary = {}

#Declaramos variables
key = str
value = str
key = ''
value = ''


#Recorremos las listas para agregar al diccionario
for index in range (0,len(list_a)):
    key = list_a[index]
    value = list_b[index]
    information_dictionary[key] = value

#Mostramos en pantalla
print(information_dictionary)