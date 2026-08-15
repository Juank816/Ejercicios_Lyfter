#Ejercicios extra de Funciones: RETORNA CUANTAS VOCALES TIENE UN STRING
'''Cree una función que reciba un string y retorne cuántas vocales contiene
Ejemplo:
Entrada:"Hola mundo"
Salida:4'''

def get_vowels(string):
    counter = 0
    
    #Pide el string
    string = input("Ingrese un string ")
    
    for index in range (0, len(string)):
        string.islower()
        if string[index] == 'a' or string[index] == 'e' or string[index] == 'i' or string[index] == 'o' or string[index] == 'u':
            counter += 1
    return counter


def main():
    #Declaramos el string
    my_string = ""
    
    #Muestra en pantalla 
    print(get_vowels(my_string))



if __name__ == "__main__":
    main()