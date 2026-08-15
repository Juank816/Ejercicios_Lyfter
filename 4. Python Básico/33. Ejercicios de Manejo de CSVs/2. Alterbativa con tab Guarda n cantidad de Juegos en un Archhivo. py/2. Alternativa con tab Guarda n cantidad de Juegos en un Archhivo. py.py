#Ejercicios de Manejo de CSVs: Prograna Permite Ingresar N cantidad de Juegos a Archivo CSV version alternativa
'''Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la 
otra para sus values.'''

'''Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba 
que guarde el archivo separado por tabulaciones en vez de por comas.'''

#Ejercicios de Manejo de CSVs: Prograna Permite Ingresar N cantidad de Juegos a Archivo CSV
'''Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
Debe incluir:
Nombre
Género
Desarrollador
Clasificación ESRB'''
import csv

def save_videogames(file_path, data):
    # Abrimos el archivo en modo escritura ('w')
    # Usamos newline='' para que no se agreguen líneas en blanco entre registros
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        # Obtenemos los nombres de las columnas con las llaves del primer registro
        headers = data[0].keys()
        # Inicializamos el escritor indicando el archivo destino y los encabezados
        writer = csv.DictWriter(file, fieldnames=headers,delimiter='\t')
        # Escribimos la primera fila en el documento con los títulos
        writer.writeheader()
        # Insertamos la lista completa de nuestros juegos
        writer.writerows(data)


def give_information(list_data):
    try:
        dictionary_information = {}
        my_list = [] 
        
        number_dictionarys = int(input(f"Ingrese el número de videojuegos que desea ingresar: "))
        print("Ingrese los siguientes datos de los videojuegos.")
        for index in range(0, number_dictionarys): # Este for lo que hace es indicar cuántos videojuegos son 
            dictionary_information = {}
            for index in range(0, len(list_data)):# Este for lo que hace es pedir los elementos de los keys 
                key = list_data[index]
                value = input(f"Ingrese {key} del videojuego: ")
                dictionary_information[key] = value
            print("Ingrese los datos del siguiente videojuego.")
            my_list.append(dictionary_information)
        return my_list
    except ValueError as ex:
        print("Valor ingressado incorrecto")


def main():
    try:
        #Esta lista es de los datos que le solicitamos al cliente para los datos
        list_data = ['Nombre','Género','Desarrollador','Clasificación ESRB']
        result = give_information(list_data)
        print(result)
        save_videogames('new_videogames.csv', result)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()