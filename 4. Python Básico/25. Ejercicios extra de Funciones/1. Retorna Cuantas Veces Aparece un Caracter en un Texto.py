#Ejercicios extra de Funciones: RETORNA CUANTAS VECES APARECE UN CARACTER
'''Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el textoEjemplo:
Entrada:

Copiar
"programacion"

"Ingrese el carácter que desea buscar:"

"o"
Salida:

Copiar
"Se a encontrado 2 veces el carácter"'''

#Funciones
def receibe_string():
    string = input(str("Ingrese un texto "))
    charter = input(str("Ingrese el caracter que desea validar del texto "))
    return counter_charter(string,charter), charter


def counter_charter(string, charter):
    counter = 0 
    
    for index in range(0, len(string)):
        if string[index] == charter:
            counter += 1
    return counter


def main():
    #Mensaje de bienvenida
    print("---- Programa que indica cuantas veces aparece una caracter en el texto ----")
    my_string = ""
    charter = ""
    
    counter, charter = receibe_string()

    print(f"Se ha encontrado {counter} veces el carácter {charter}")
    


if __name__ == "__main__":
    main()