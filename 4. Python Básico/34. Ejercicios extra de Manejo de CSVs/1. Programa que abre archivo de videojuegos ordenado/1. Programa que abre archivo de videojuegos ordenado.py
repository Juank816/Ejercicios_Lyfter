#Ejercicios extra de Manejo de CSVs: Abre información de archivo de videojuegos de manera legible
'''Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
Lea cada línea usando csv.reader()
Muestre el contenido en pantalla de forma legible, línea por línea
Ejemplo:
Nombre: Grand Theft Auto IV
Género: Accion
Desarrollador: Rockstar Games
Clasificación: M
'''
import csv

def read_videogames(file_path):
    with open(file_path, 'r', encoding='utf-8' ) as file:
        # DictReader convierte cada fila en un diccionario
        reader = csv.DictReader(file)
        for games in reader:
            for key, value in games.items():
                print(f"{key}: {value}")

def main():
    try:
        read_videogames('new_videogames_read1.csv')
    except Exception as ex:
            print(ex)


if __name__ == "__main__":
    main()