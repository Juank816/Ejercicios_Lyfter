#TEMA: Diccionarios
#Como accesar a datos 

'''Como vimos en Tipos de Datos, podemos accesar a los elementos de un diccionario usando paréntesis cuadrados
con su key adentro.'''

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information['description'])

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('description'))

#Tenemos la iteración
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country, capital in europe_capitals_by_country.items():
	print(f'{country} : {capital}')

#También podemos accesar solo a los keys o a los values de un diccionario usando el método llamado igual a 
# estos.


#Iterando el keys
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country.keys():
	print(country)

#Iterando el Values
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for capital in europe_capitals_by_country.values():
	print(capital)
 
 
#Con esto podemos imprimir la informacion anidada
course_information = {
    'title': 'Introduction to DBs',
    'description': 'Here we review the basics of SQL Databases',
    'length_in_minutes': {
        "time1": "10 minutos",
        "time2": "20 minutos",
    },
}

# Accedemos al sub-diccionario usando ['length_in_minutes']
# y le aplicamos .items()
for clave_tiempo, valor_tiempo in course_information['length_in_minutes'].items():
    print(f"Key: {clave_tiempo} -> Valor: {valor_tiempo}")

# Comprueba si el valor es otro diccionario
for clave, valor in course_information.items():
    if isinstance(valor, dict):  # Comprueba si el valor es otro diccionario
        print(f"\n--- Sub-diccionario de '{clave}' ---")
        for sub_clave, sub_valor in valor.items():
            print(f"  {sub_clave}: {sub_valor}")
    else:
        print(f"{clave}: {valor}")