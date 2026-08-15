#Ejercicios extra de Manejo de Archivos: Convierte cada Linea de un Archivo en Mayusucula
'''Cree un programa que:
Lea un archivo línea por línea
Convierta cada línea a mayúsculas
Escriba el contenido en un nuevo archivo'''
def read_complete_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError as ex:
            print("No se encontró el archivo")


def read_file_by_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError as ex:
        print("No se encontró el archivo") 


def convert_uppercase(content):
    new_list = []
    for line in content:
        new_list.append(line.upper())
    result = "".join(new_list) #Convierte la lista recibida desde el inicio en string
    return result


def write_new_file(path, text):
    try:
        with open(path, 'w', encoding='utf-8') as file: 
            file.write(text)
    except FileNotFoundError:
                print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para acceder a este archivo.")


def main():
    try:
        my_list = read_file_by_lines(r"MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 3 Convierte cada Linea de un Archivo en Mayusucula\Texto.txt")
        my_string = convert_uppercase(my_list)
        write_new_file(r'MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 3 Convierte cada Linea de un Archivo en Mayusucula\NewText.txt', my_string)
        result = read_complete_file(r'MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 3 Convierte cada Linea de un Archivo en Mayusucula\NewText.txt')
        print(result)
    except Exception as ex:
        print (ex)


if __name__ == "__main__":
    main()