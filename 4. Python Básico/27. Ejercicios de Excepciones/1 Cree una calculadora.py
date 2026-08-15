#Ejercicios de Excepciones: Cree una calculadora por linea de comando

'''Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué 
operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir 
por el actual. El resultado debe pasar a ser el nuevo numero actual. Debe de mostrar mensajes de error si el
usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.'''

#Par obtener lo números
def give_number():
    print("Por favor ingrese el segundo número: ")
    number2 = int(input("Número 2: "))
    
    return number2


#Operaciones básicas
def addition(number1):
    addition = 0
    try:
        number2 = give_number()
        addition = number1 + number2
        return addition
    except ValueError:
        print("Ha ocurrido un error, se ha ingresado un valor incorrecto.")


def subtraction(number1):
    try:
        subtraction = 0
        number2 = give_number()
        subtraction = number1 - number2
        return subtraction
    except ValueError:
        print("Ha ocurrido un error, se ha ingresado un valor incorrecto.")


def multiplication(number1):
    try:
        multiplication = 0
        number2 = give_number()
        multiplication = number1 * number2
        return multiplication
    except ValueError:
        print("Ha ocurrido un error, se ha ingresado un valor incorrecto.") 


def division(number1):
    try:
        division = 0
        number2 = give_number()
        division = number1 / number2
        return division
    except ValueError:
        print("Ha ocurrido un error, se ha ingresado un valor incorrecto.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")


#Función del menú
def menu(actual_number):
    while True:
        print(
            "1. Suma\n"
            "2. Resta\n"
            "3. Multiplicación\n"
            "4. División\n"
            "5. Borrar resultado\n"
            "6. Salir \n"
            )
        try:
            option = int(input("Por favor ingresa el número de la opción que desea realizar: "))
            match option:
                case 1:
                    result = addition(actual_number)
                    if result is not None:
                        print(f"El resultado de la suma es: {result}")
                        actual_number = result
                        print(f"Ahora el número actual es: {actual_number}")
                case 2:
                    result = subtraction(actual_number)
                    if result is not None:
                        print(f"El resultado de la resta es: {result}")
                        actual_number = result
                        print(f"Ahora el número actual es: {actual_number}")
                case 3:
                    result  = multiplication(actual_number)
                    if result is not None:
                        print(f"El resultado de la multiplicación es: {result}")
                        actual_number = result
                        print(f"Ahora el número actual es: {actual_number}")
                case 4:
                    result = division(actual_number)
                    if result is not None:
                        print(f"El resultado de la división es: {result}")
                        actual_number = result
                        print(f"Ahora el número actual es: {actual_number}")
                case 5:
                    actual_number = 0
                    print("El resultado ha sido eliminado ")
                case 6:
                    print("Saliendo")
                    break
                case _:
                    print("Opción no valida")
        except ValueError:
            print("Ha ocurrido un error, no se ha selccionado ninguna opción valida.")
    return actual_number


def main():
    actual_number = 10
    
    
    print("---- Calculadora ----")
    actual_number = menu(actual_number)
    print(f"El número actual es: {actual_number}")


if __name__ == "__main__":
    main()