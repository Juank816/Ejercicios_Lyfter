#Ejercicios extra de Diccionarios: DICCIONARIO QUE GUARDE EL TOTAL DE VENTAS DE CADA UPC
'''Dada una lista de ventas con la siguiente información:
date
customer_email
items
Y cada item teniendo la siguiente información:
name
upc
unit_price
Cree un diccionario que guarde el total de ventas de cada UPC.'''

print("---- Diccionario que guarda la información de ventas   ----")

#Declaramos el diccionario que guarda la información 
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

#Declaramos diccionario
result = {}

#Declaramos variables
items = str
upc = str
items = ''
upc = ''
price = 0
total_price = 0  


#Proceso
for sale in sales:
    items = sale['items']
    for product in items:
        upc = product['upc']
        price = product['unit_price']
        if upc not in result:
            result[upc] = price
        else:
            result[upc] = result[upc] + price


#Muestra el resultado
print(result)