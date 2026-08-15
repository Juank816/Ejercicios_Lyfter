#Manejo de CSVs:Escritura de CSV ✍️


'''Así como hicimos la lectura de la lista de series, también podemos generar una nueva lista desde el código. 
Para eso empleamos la herramienta DictWriter, la cual nos permite registrar información estructurada fila 
por fila en un archivo CSV.'''

'''Ejemplo de Escritura 🎬
Si queremos crear un nuevo archivo CSV con un top 10 de series animadas, 
podemos hacerlo como se muestra a continuación:'''  

import csv

def save_series_ranking(file_path, data):
    # Abrimos el archivo en modo escritura ('w')
    # Usamos newline='' para que no se agreguen líneas en blanco entre registros
    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        # Obtenemos los nombres de las columnas con las llaves del primer registro
        headers = data[0].keys()

        # Inicializamos el escritor indicando el archivo destino y los encabezados
        writer = csv.DictWriter(file, fieldnames=headers)

        # Escribimos la primera fila en el documento con los títulos
        writer.writeheader()

        # Insertamos la lista completa de nuestras series
        writer.writerows(data)

# Lista de diccionarios con las series animadas seleccionadas
top_10_ranking = [
    {
        "Name": "Avatar: The Last Airbender",
        "Platform": "Nickelodeon",
        "Score": 9.3,
        "Episodes": 61,
        "Seasons": 3,
        "Genre": "Animation",
        "Year": 2005,
        "Director": "Michael Dante DiMartino",
    },
    {
        "Name": "Rick and Morty",
        "Platform": "Adult Swim",
        "Score": 9.1,
        "Episodes": 71,
        "Seasons": 7,
        "Genre": "Comedy",
        "Year": 2013,
        "Director": "Justin Roiland",
    },
    {
        "Name": "Batman: The Animated Series",
        "Platform": "Fox Kids",
        "Score": 9.0,
        "Episodes": 85,
        "Seasons": 4,
        "Genre": "Action",
        "Year": 1992,
        "Director": "Bruce Timm",
    },
    {
        "Name": "Arcane",
        "Platform": "Netflix",
        "Score": 9.0,
        "Episodes": 9,
        "Seasons": 1,
        "Genre": "Action",
        "Year": 2021,
        "Director": "Pascal Charrue",
    }
]


save_series_ranking('new_series_ranking.csv', top_10_ranking)