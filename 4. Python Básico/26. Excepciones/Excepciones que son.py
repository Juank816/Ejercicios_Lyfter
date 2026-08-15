#Excepciones
'''Que son?
Hemos sido testigos de como existen distintos tipos de error que pueden pasar durante la ejecución del código.
Es decir, mientras el código está corriendo. No antes.
A este tipo de errores no sintácticos le llamamos Exceptions.
Es decir que son errores que suceden con código escrito con sintaxis valida.
Esto no es una excepción ya que el código nunca llega a ejecutarse:'''

# def main():
#     print('Ejecutando...')
#     &^&*&^*&^


# if __name__ == '__main__':
# 	main()

'''Index error '''
# def main():
#     my_4_elements = ["One", "Two", "Three", "Four"]

#     print(my_4_elements[3])
#     print(my_4_elements[4])


# if __name__ == '__main__':
# 	main()
'''
La mayoría de excepciones tienen un nombre.
En el caso anterior, tenemos una excepción de tipo IndexError.
Otro ejemplo es cuando intentamos convertir un string no numeral a un int:'''
def main():
    my_first_string = "2"
    my_second_string = "Hello"
	
    my_first_int = int(my_first_string)
    print(my_first_int + 2)
	
    my_second_int = int(my_second_string)
    print(my_second_int + 2)


if __name__ == '__main__':
	main()