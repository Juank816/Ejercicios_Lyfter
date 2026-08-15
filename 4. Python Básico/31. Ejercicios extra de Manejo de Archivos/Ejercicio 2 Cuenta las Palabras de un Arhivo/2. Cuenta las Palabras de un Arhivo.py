#Ejercicios extra de Manejo de Archivos:Programa que arba un archivo y cuente cuantas palabras tiene en total

'''Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
(Considere que las palabras están separadas por espacios y/o saltos de línea)'''

def read_file_by_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError as ex:
        print("No se encontró el archivo")


def convert_string(content):
    new_list = []
    for line in content:
        new_list.append(line.strip()) #Agrega y quita los saltos de línea
    string = " ".join(new_list) #Convierte la lista recibida desde el inicio en string
    return string
    #print(string)


def number_of_words(string):
    words = string.split()
    return len(words)


def main():
    try:
        content = read_file_by_lines(r'MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 2 Cuenta las Palabras de un Arhivo\CuantasPalabras.txt')
        my_string = convert_string(content)
        total = number_of_words(my_string)
        print(f"Este archivo contiene {total} palabras")
    except Exception as ex:
        print (ex)


if __name__ == "__main__":
    main()