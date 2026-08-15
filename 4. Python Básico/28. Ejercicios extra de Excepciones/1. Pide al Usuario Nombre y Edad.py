#Ejercicios extra de Excepciones: Pide al usuario su nombre 
'''Pida al usuario su nombre
Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
Ejemplo:
Entrada:


Entrada:"Ingrese su nombre: 5
Salida:"El nombre no puede ser un número"'''

def give_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    return name


def give_age():
    try:
        return int(input("Ingrese su edad: "))
    except ValueError:
        raise ValueError("Debe ingresar un número válido")

def main():
    try:
        name = give_name()
        age = give_age()
        print(f"Hola {name}, su edad es {age}")
    except ValueError as ex:
        print(ex)

if __name__ == "__main__":
    main()