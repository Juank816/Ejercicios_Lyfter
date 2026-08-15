#Manejo de listas: AGREGAR DATOS

my_pets_list = [
	'dog',
	'cat',
]

my_pets_list.append('rabbit')
print(my_pets_list)

#También podemos usar el método insert para agregar un elemento en un índice especifico:
#//////////////////////////////////////////////////////////////////////////////////////
courses_list = [
	'Computers',
	'Algorithms',
	'Python',
	'Web Development',
]

courses_list.insert(2, 'Databases')
print(courses_list)

#También podemos usar el método insert para agregar un elemento en un índice especifico:
#//////////////////////////////////////////////////////////////////////////////////////
first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list)
print(first_list)