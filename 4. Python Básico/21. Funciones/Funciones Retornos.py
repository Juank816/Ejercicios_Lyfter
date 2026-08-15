#TEMA: Funciones (PARAMETROS Y RETORNOS)
#RETORNOS

'''La palabra return nos permite decidir qué valor o valores serán el output de la función.
Pueden haber varios return en una función, pero el primero que se ejecute es el que terminará la función.
Nada de lo que haya después de él se ejecutará.
Parecido a un break en un ciclo.
Estos outputs los podemos guardarlos en variables o usarlos como valores comunes y corrientes.
Por ejemplo, cuando guardamos el output de un input en una variable.
Por ejemplo, podemos crear una función que sume tres números y retorne su resultado:'''

def sum_three_numbers(number1, number2, number3):
    return number1 + number2 + number3


result = sum_three_numbers(600, 700, 800)
print(result)

#Tenemos este otro ejemplo
#O podemos crear una función que encuentre el máximo de 2 números y lo retorne:
def get_max_of_two_numbers(number1, number2):
    if number1 > number2:
        return number1

    return number2


print(get_max_of_two_numbers(3, 7))
# Podemos notar es que estamos encadenando dos funciones, print y get_max_of_two_numbers.
# Esto es porque ya sabemos que esa función va a retornar un valor.
# Y una función ejecutada es igual a utilizar un valor o una variable.
# Podemos usar llamados a funciones como parámetros para otras funciones, ya que el código se 
# ejecutará de adentro hacia afuera.
# Es exactamente lo mismo a hacer esto:
def get_max_of_two_numbers(number1, number2):
    if number1 > number2:
        return number1

    return number2


result = get_max_of_two_numbers(4, 15)
print(result)
