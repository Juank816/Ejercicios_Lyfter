#Excepciones: Buenas prácticas 
'''Siempre debemos hacer try de instrucciones que sabemos pueden ocasionar una excepción.
Si un error puede pasar, va a pasar!
Siempre hay que estar a la defensiva.
Lo mejor es no declarar variables dentro de un try ya que si este falla, la variable no existirá y podrá 
ocasionar errores en futuras instrucciones.'''

def main():
    my_list = [
	'2',
	'Hello'
	]
    index_to_use = 4
	
    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)   
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
	
    print(element_to_int)


if __name__ == '__main__':
	main()

#Es mejor declararlas antes del try con valores placeholder.
def main():
    my_list = [
	'2',
	'Hello'
	]
    index_to_use = 4
	
    list_element_to_convert = '0'
    element_to_int = 0
    
    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)
        print(list_element_to_convert)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
	
        print(list_element_to_convert)


if __name__ == '__main__':
	main()

'''Generalmente es buena practica el envolver todo el programa en un try - except general, y dentro de cada 
función se usar try - excepts especificos para cada tipo de error.'''
def function_1():
    try:
        some_logic_with_value_errors()
    except ValueError as ex:
        print(f'An error ocurred in function_1')


def function_2():
	try:
        some_logic_with_index_errors()
    except IndexError as ex:
		print(f'An error ocurred in function_2')


def main():
	try:
        function_1():
        function_2():

    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')


if __name__ == '__main__':
	main()
#Nunca debemos usar un except para un happy path.
# Está muy mal visto ya que está en contra del uso de la sintaxis.
# Una vez despidieron a un compañero por esto.
# Por ejemplo, usarlo para validar que un texto no sea un número:

'''INCORRECTO'''
name = input("Ingrese su nombre: ")
try:
    int(name)
	# unhappy path
    print("Su nombre no puede ser un numero!")
except Exception as error:
	# happy path
    edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
    empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")

'''CORRECTO'''
try:
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError()
except Exception as error:
	# unhappy path
    print("Su nombre no puede ser un numero!")

# happy path
edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")