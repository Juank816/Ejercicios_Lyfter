#Ejercicios de Funciones: CONCEPTO SCOPE
'''Experimente con el concepto de scope:
Intente acceder a una variable definida dentro de una función desde afuera.
Intente acceder a una variable global desde una función y cambiar su valor.'''

global_variable = 20

def get_information():
    number_in_funtion = 10
    print(number_in_funtion)

'''1.Intente acceder a una variable definida dentro de una función desde afuera.'''
#print(number_in_funtion) #/ No deja debido a que en este caso solo está declarada en la 
#función
get_information()

'''2.Intente acceder a una variable global desde una función y cambiar su valor. '''
def second_funtion(parameter1):
    parameter1 = 15
    return parameter1

print(second_funtion(global_variable))
print(global_variable)

#Corrección de la parte 2 con la palabra clabe global 
x = 10  # global variable

def fun():
		global x  # referencing the global variable x
		x = 20  # modifying the global variable

fun()
print(x)

