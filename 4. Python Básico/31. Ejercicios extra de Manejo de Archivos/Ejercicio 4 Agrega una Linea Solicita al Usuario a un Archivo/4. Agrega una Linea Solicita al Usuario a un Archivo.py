#Ejercicios extra de Manejo de Archivos: Agrega una Linea Solicita al Usuario a un Archivo
'''Cree un programa que:
Pida al usuario una línea de texto
Agregue esa línea al final de un archivo existente
Si el archivo no existe, lo crea automáticamente'''
def append_to_file(path, extra_text):
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write("\n" + extra_text)
        print("El texto se agrega al final del archivo sin borrar lo anterior")
    except PermissionError:
        print("No tienes permisos para escribir en el archivo.")


def give_information():

    print("Este programa agrega una línea al final de un archivo.")
    string = input("Ingrese una línea de texto: ")
    return string


def main():
    try:
        my_string = give_information()
        ###############
        append_to_file('File.txt', my_string)
    except Exception as ex:
        print (ex)


if __name__ == "__main__":
    main()