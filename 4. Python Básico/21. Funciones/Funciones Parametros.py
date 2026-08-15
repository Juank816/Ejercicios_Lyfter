#TEMA: Funciones (PARAMETROS Y RETORNOS)

def print_parameters(parameter_1, parameter_2, parameter_3):
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')


print_parameters(50, 'Hello', 90)
print('-')
print_parameters([4, 5, 6], 'World', 'Inside')
print('-')
print_parameters('A', 'Function', True)


# Otro detalle útil es que podemos definir parámetros opcionales en las funciones.
# Es decir, hacer que ciertos parámetros sean opcionales y tengan un valor por defecto en caso de que 
# no se especifiquen a la hora de ejecutarlas.
# Estos parámetros opcionales deben ir después de los requeridos.
# Esto lo hacemos justo como al darle un valor a una variable.
def print_sum_of_numbers(number_a, number_b=5):
    print(number_a + number_b)


print_sum_of_numbers(4)
