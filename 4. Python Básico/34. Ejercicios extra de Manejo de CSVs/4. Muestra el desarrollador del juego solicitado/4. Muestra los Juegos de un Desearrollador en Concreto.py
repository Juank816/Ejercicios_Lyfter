#Ejercicios extra de Manejo de CSVs: Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
'''Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
Ejemplo:
Videojuegos desarrollados por Ubisoft:
- Assassin's Creed II (Clasificación: M, Género: Aventura)
- Rayman Legends (Clasificación: E, Género: Plataforma)'''
import csv 

def give_information():
    print("Bienvenido al programa. Con este programa puede verificar los juegos por empresa que desarrollo el/los juego/s")
    string = input("Por favor ingresar el nombre de la empresa que desarrolladora: ")
    string = string.capitalize()
    return string


def read_videogames(file_path, name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(f"Los juegos desarrollados por {name}: ")
            for games in reader:
                if games['desarrollador'] == name:
                    print(f"{games['nombre']} (Clasificación: {games['clasificacion']}, Género: {games['genero']}")
    except FileNotFoundError:
        print("El archivo no existe.")


def main():
    try:
        name = give_information()
        print(name)
        read_videogames('new_videogames.csv', name)
    except Exception as ex:
            print(ex)


    
    main()