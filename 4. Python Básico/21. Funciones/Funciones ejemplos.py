#TEMA: Funciones
#Aprende qué son las funciones y cómo usarlas para organizar tu código de mejor manera.

'''Qué son?
Las funciones o métodos (una definición de función un poco mas especifica que veremos después) nos permiten
crear bloques de código reutilizables.'''


#Por ejemplo, puedo crear una función que llame un print para imprimir Hello World y Mi primera funcion.
# A esta función la llamaré print_hello_world:
def print_hello_world():
	print("Hello World!")
	print("Mi primera funcion")

print_hello_world()
print_hello_world()

# Las funciones pueden tener cualquiera de las instrucciones que hemos estado usando hasta ahora.
# Incluso pueden tener sus propias variables y llamar a otras funciones.
def calculate_salary():
	worked_hours = int(input("Ingrese sus horas trabajadas: "))
	hour_rate = int(input("Ingrese su tarifa por hora: "))

	salary = worked_hours * hour_rate
	
	print(f'Su salario sera de {salary}')


calculate_salary()