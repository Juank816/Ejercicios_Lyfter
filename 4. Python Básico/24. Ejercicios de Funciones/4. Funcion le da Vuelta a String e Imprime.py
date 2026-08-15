#Ejercicios de Funciones: RETORNA UN STRING AL REVÉS
'''Cree una función que le dé la vuelta a un string y lo retorne.
Esto ya lo hicimos en iterables.
“Hola mundo” → “odnum aloH”'''


#Funciones
def get_string():
    reversed_string = ""
    string1 = "Hola mundo"
    
    for index in range(len(string1)-1, -1, -1):
        reversed_string = reversed_string + string1[index]
        
    return reversed_string


def main():
    print("---- Programa Imprime String al Revés ----")
    print (get_string())


if __name__ == "__main__":
    main()