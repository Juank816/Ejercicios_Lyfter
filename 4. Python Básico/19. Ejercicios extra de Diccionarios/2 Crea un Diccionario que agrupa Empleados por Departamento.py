#Ejercicios extra de Diccionarios: AGRUPA COMPAÑEROS POR DEPARTAMENTO
'''Agrupar empleados por departamento
Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe 
los empleados por su departamento:'''

print("---- Programa agrupa empleados por departamento  ----")

#Declaramos diccionario
departments = {
    
}

#Declaramos la lista
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
#Declaramos variables
key = str
value = str
department = str
key = ''
value = ''
department = ''

#for index in employees:
#    print(index["department"])

#Nos sirve para agregar la key o departamento a diccionario
for index in employees:
    department = index['department']
    if department not in departments:
        departments[department] = []  
    
    #departments[department] = [value]
    departments[department].append(index["name"])



print(departments)