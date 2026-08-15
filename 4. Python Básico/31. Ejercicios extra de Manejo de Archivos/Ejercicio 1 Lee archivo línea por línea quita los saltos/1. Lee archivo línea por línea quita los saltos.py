#Ejercicios extra de Manejo de Archivos: Lee un archivo línea por línea y luego lo imprime en un solo renglón 
#quita los saltos

'''Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo
el contenido en un solo renglón en un nuevo archivo'''
def read_complete_file(path):
    try:
        # Usamos 'with' para un manejo seguro del archivo
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError as ex:
            print("No se encontró el archivo")


def read_file_by_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            #print(lines)
            for number, line in enumerate(lines, start=1):
                        # Usamos strip() para remover los saltos de línea y limpiar espacios
                        print(f"Line {number}: {line.strip()}")
        result = lines
        return result
    except FileNotFoundError as ex:
        print("No se encontró el archivo")




def remove_break_lines(content):
    
    new_list = []

    for line in content:
        new_list.append(line.strip())
    #print(new_list)
    result =  " ".join(new_list)
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
        content = read_file_by_lines(r'D:\Curso Lyfter\MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 1 Lee archivo línea por línea quita los saltos\texto1.txt')
        result = remove_break_lines(content)
        write_new_file(r'D:\Curso Lyfter\MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 1 Lee archivo línea por línea quita los saltos\NewText.txt', result)
        print(f"La salida de lo solicitado es: {read_complete_file(r'D:\Curso Lyfter\MÓDULOS\4. Python Básico\31. Ejercicios extra de Manejo de Archivos\Ejercicio 1 Lee archivo línea por línea quita los saltos\NewText.txt')}")
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()