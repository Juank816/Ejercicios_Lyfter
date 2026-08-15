#Ejercicios de Funciones: DOS FUNCIONES QUE IMPRIMEN COSAS DISTINTAS
'''Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.'''

def print_first_string ():
    print(f"¡Buenos días!")
    print_second_string()

def print_second_string():
    print("¿Cómo están?")

def main():
    print_first_string() 


if __name__ == "__main__":
    main()





