#Ejercicios de Funciones: RETORNA UN STRING AL REVÉS
'''Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”'''

#Funciones
def get_cases():
    counter_upper = 0
    counter_lower = 0
    my_string = "I love Nación Sushi"
    result = ""
    
    for index in range (0, len(my_string)):
        if my_string[index].isupper():
            counter_upper += 1
        elif my_string[index].islower():
            counter_lower += 1
    
    result = (f"There’s {counter_upper} upper cases and {counter_lower} lower cases")
    return result


def main():
    print("---- Programa que muestra cuántas mayúsculas y minúsculas tiene un string ----")
    print(get_cases())


if __name__ == "__main__":
    main()