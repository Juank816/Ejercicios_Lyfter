#Ejercicios de Diccionarios: DICCIONARIO QUE USA UNA LISTA PARA ELIMINAR KEYS DEL DICCIONARIO
'''Cree un programa que use una lista para eliminar keys de un diccionario.'''

print("---- Programa usa una lista para eliminar keys de un diccionario  ----")

#Declaramos las lista
list_of_keys = ['access_level', 'age']

#Declaramos el diccionario que guarda la información solicita 
employee  = {
    'name' : 'John',
    'email' : 'john@ecorp.com',
    'access_level' : 5,
    'age' : 28
}

#Recorremos el diccionario para eliminar las keys
for index in list_of_keys:
    employee.pop(index)

print(employee)