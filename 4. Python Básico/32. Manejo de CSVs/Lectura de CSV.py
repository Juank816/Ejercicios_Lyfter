#Manejo de CSVs: A lo largo de nuestro camino como desarrolladores, tendremos la necesidad de guardar, analizar y transmitir la información que producen nuestros programas.
# Si bien existen formatos avanzados, muchas veces necesitamos una forma sencilla y directa de compartir datos. 
# Para ello se han creado múltiples formatos, entre ellos el CSV, que destaca por ser ligero, ordenado y universalmente aceptado. 
# Esta herramienta la vamos a usar de forma recurrente cuando trabajemos con análisis de datos o importaciones masivas en Python.

'''Un archivo CSV es una tabla de datos simplificada al máximo. Sus siglas significan 
“Comma Separated Values” (Valores Separados por Comas). Es una forma muy común de guardar datos 
estructurados en texto plano, donde cada línea representa una fila y cada columna se separa con una coma.'''

#Imaginemos que estamos recopilando información sobre las 10 mejores series de plataformas 
# de streaming de todos los tiempos. Un archivo top_series.csv se vería así:

'''Name,Platform,Score,Episodes,Seasons,Genre,Year,Director
Breaking Bad,AMC,9.5,62,5,Drama,2008,Vince Gilligan
The Wire,HBO,9.3,60,5,Crime,2002,David Simon
Band of Brothers,HBO,9.4,10,1,War,2001,Steven Spielberg
Chernobyl,HBO,9.4,5,1,Drama,2019,Craig Mazin
The Sopranos,HBO,9.2,86,6,Crime,1999,David Chase
Game of Thrones,HBO,9.2,73,8,Action,2011,David Benioff
Avatar: The Last Airbender,Nickelodeon,9.3,61,3,Animation,2005,Michael Dante DiMartino
Better Call Saul,AMC,9.0,63,6,Crime,2015,Vince Gilligan
The Office,NBC,9.0,201,9,Comedy,2005,Greg Daniels
Stranger Things,Netflix,8.7,34,4,Sci-Fi,2016,The Duffer Brothers'''

#Lectura de CSV 📖
'''En el proceso de leer un archivo CSV cada línea del documento representa un registro. 
En un CSV podemos procesar cada fila y acceder a los datos exactos que nos interesan, como 
la nota, el año de estreno o la plataforma. Para lograr esto en Python, utilizamos el módulo csv 
y una herramienta llamada DictReader, la cual convierte cada fila del archivo en un diccionario,
usando los encabezados que definimos en la primera línea como las claves.'''
import csv

def read_series(file_path):
    # Abrimos el archivo en modo lectura con soporte para utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        # DictReader convierte cada fila en un diccionario
        reader = csv.DictReader(file)

        for series in reader:
            # Accedemos a los datos usando los nombres de las columnas como claves
            print(f"Top choice: {series['Name']} on {series['Platform']} - Score: {series['Score']}/10.")

read_series('ArchivoCSV.csv')