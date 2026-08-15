#Ejercicios extra de Diccionarios: AGRUPA TOTAL VENDIDO DE PRODUCTOS
'''Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que 
acumule el total por categoría.'''

print("---- Programa agrupa total vendido de productos  ----")

#Declaramos diccionario
categorys = {}

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

#Declaramos variables
category = str
category = ''
price = 0

#Nos sirve para agregar la key o categoría a diccionari
for index in products:
    category = index['category']
    price = index['price']
    if category not in categorys:
        categorys[category] = price
    else:
        categorys[category] = categorys[category] + price

#Muestra en pantalla el resultado
print(categorys)
