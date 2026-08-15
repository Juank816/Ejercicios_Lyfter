#Ejercicios de Manejo de Archivos: Programa que lee nombres de canciones, luego los ordena alfabeticamente en
# otro archivo

'''Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo 
los mismos nombres ordenados alfabéticamente.'''
def ordenate_songs(content):
    content.sort()
    return content


def write_new_file(path, text):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for line in text:
                file.write(line.strip() + "\n")
    except FileNotFoundError:
            print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para acceder a este archivo.")


def give_songs(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            for number, line in enumerate(content, start=1):
                #Usamos strip() para remover los saltos de línea y limpiar espacios
                print(f"Line {number}: {line.strip()}")
            return content
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
            print("No tienes permiso para acceder a este archivo.")


def main():
    try:
        content = give_songs('Canciones.txt')
        content_ordenate = ordenate_songs(content)
        write_new_file('ordenate songs.txt', content_ordenate)
        print("-------------- Imprime el nuevo Archivo----------------")
        give_songs('ordenate songs.txt')
    except FileNotFoundError as ex:
        print(ex)
    except PermissionError as ex:
        print(ex)


if __name__ == "__main__":
    main()