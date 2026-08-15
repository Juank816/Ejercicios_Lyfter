#Ejercicios extra de Manejo de CSVs: Abre información de archivo de videojuegos por clasificación
'''Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación'''
import csv
def give_calasification():
    return input("Por favor ingrese al clasificación que desea encontrar: ")


def read_videogames(file_path,clasification):
    try:
        clasification = clasification.upper()
        new_list = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for games in reader:
                if games['clasificacion'] == clasification:
                    new_list.append(games['nombre'])
            print(f"Los juegos que son de clasificación {clasification} es/son: {new_list}")
    except FileNotFoundError:
        print("El archivo no existe.")
    except KeyError as ex:
        print(f"La llave no existe en el diccionario: {ex}")


def main():
    try:
        clasification = give_calasification()
        read_videogames('new_videogames.csv', clasification)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()