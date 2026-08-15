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
