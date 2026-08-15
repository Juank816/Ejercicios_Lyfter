#TEMA: Diccionarios
#Como agregar o eliminar datos 

'''
Debido a que los datos de los diccionarios están atados a keys, debemos accesar a la key que queremos llenar 
(aunque no exista) y darle un valor'''

#Agregar datos
user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)

#Eliminar datos
student_information = {
	'first_name': 'Harry',
	'last_name': 'Potter',
	'age': 17,
}

deleted_item = student_information.pop('last_name')
print(student_information)
print(f'Deleted item: {deleted_item}')