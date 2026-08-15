#Ejercicios extra de Manejo de CSVs: Muestra cantidad de generos por juego
'''Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Cuente cuántos videojuegos hay de cada género
Muestre el resultado de forma ordenada
Ejemplo:
Géneros encontrados:
Acción: 5
Aventura: 3
Deportes: 4
...'''
import csv

def counter_videogames(genders):
    result = 0
    result1 = 0
    result2 = 0 
    for counter in genders:
        if counter == 'Accion':
            result = result + 1
        elif counter == 'RPG':
            result1 = result1 + 1
        elif counter == 'Deportes':
            result2 = result2 + 1 
    print(f"Géneros encontrados:\n Acción: {result}\n Deportes: {result1}\n RPG: {result2}")


def read_videogames(file_path):
    try:
        gender = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for gen in reader:
                gender.append(gen['genero'])
            return gender
    except FileNotFoundError:
        print("El archivo no existe.")
    except KeyError as ex:
        print(f"La llave no existe en el diccionario: {ex}")


def main():
    try:
        genders = read_videogames('new_videogames.csv')
        #print(genders)
        counter_videogames(genders)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()