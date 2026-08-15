#Excepciones: Cómo Manejarlas 
'''Cómo Manejarlas?
Todos los códigos tienen happy paths (caminos felices) en los que el usuario usa el programa exactamente como 
lo planeamos.
Sin embargo, también existen los unhappy paths (caminos no felices) en los que el usuario hace algo no planeado
que causa una excepción.
Por ejemplo, escribir “Hola” cuando le pedimos un número.
Como desarrolladores tenemos que tomar en cuenta tanto los happy paths como los unhappy paths y manejar ambos 
para que el programa no se caiga.Esto lo podemos lograr gracias a la sintaxis de try y except.
En la mayoría de los lenguajes es try y catch, pero el resto de la sintaxis suele ser igual.
Esta nos permite agregar instrucciones que podrían arrojar un Exception y definir instrucciones para qué hacer
en caso de que eso suceda.
Veamos el mismo ejemplo con un try - except implementado:'''

# def main():
# 	my_second_string = 'Hello'

# 	try:
# 		my_second_int = int(my_second_string)
# 	except ValueError:
# 		print('Hubo un error al convertir este string a numero!')   


# if __name__ == '__main__':
# 	main()

'''Tambien podemos declarar varios excepts en un solo try para manejar distintos tipos de excepciones distintos
dentro del mismo bloque de código:'''
# def main():
# 	my_list = [
# 	'2',
# 	'Hello'
# 	]
# 	index_to_use = 4
	
#     try:
# 	    list_element_to_convert = my_list[index_to_use]
#         element_to_int = int(list_element_to_convert)
#         print(element_to_int)
# 	except IndexError as error:
# 	    print(f'El indice a usar no existe en la lista. Error: {error}')
# 	except ValueError as error:
# 	    print(f'El elemento de la lista no es un numero valido. Error: {error}')


# if __name__ == '__main__':
# 	main()


