#PROYECTO: Sistema de Control de Estudiantes
'''En este apartado tenemos las acciones o funciones mas cortas incluídas en el menú por ejemplo.'''

#En este apartado se hacen las importaciones necesarias
import os
import csv
# from encodings import utf_8_sig
# from unittest.mock import patch

'''CASE 1'''
# 1.Función que le solicita al usuario cuántos alumnos debe ingresar
def give_number_students():
    while True:
        try:
            number_students = int(input("Enter the number of students you want to add: ")) #Ingrese la cantidad de estudiantes que desea agregar
            if number_students > 0:
                return number_students
            print("Please enter a number greater than 0.") #Por favor, ingrese un número mayor a 0.
        except ValueError:
            print("Invalid input. Please enter a valid whole number.") #Entrada no válida. Por favor, ingrese un número entero válido.

# 2. Función que se encarga de validar  si un número está dentro del rango solicitado
def check_if_number_100(signature):
    while True:
        try:
            number = int(input(f"Enter the {signature} (0-100): ")) #Ingrese la nota de {signature} (0-100)
            if 0 <= number <= 100:
                return number 
            print(f"You must enter a grade from 0 to 100 for {signature}.") #Debe ingresar una nota de 0 a 100 para {signature}.
        except ValueError as ex:
            print(f"You must enter a grade from 0 to 100 for {signature}.") #Debe ingresar una nota de 0 a 100 para {signature}.


# 3.Función que se encarga de recopilar la información ingresada por el usuario
def give_information_students(number_students):
    all_students = {}


    for student in range(0, number_students):
        #Se solicita la información al usuario
        name = str(input("Enter your full name: ")) #Ingrese su nombre completo:
        group = str(input("Enter your section: ")) #Ingrese su sección: 
        spanish_grade = check_if_number_100("spanish grade")
        english_grade = check_if_number_100("english grade")
        social_studios_grade = check_if_number_100("social studios grade")
        science_grade = check_if_number_100("science grade")

        #En este apartado se agrega la información al diccionario
        all_students[name] = {
            'group': group,
            'spanish_grade': spanish_grade,
            'english_grade': english_grade,
            'social_studios_grade': social_studios_grade,
            'science_grade': science_grade
        }
        input("Press any key to continue") #Presione alguna tecla para continuar
    return all_students


'''CASE 2'''
# 1.Función que se encarga de mostrar la información ingresada por el usuario
def show_information_add(user_information):
    for name, data in user_information.items():
        print(f"Name: {name}")
        print(f"Group: {data['group']}")
        print(f"Spanish Grade: {data['spanish_grade']}")
        print(f"English Grade: {data['english_grade']}")
        print(f"Social Studies Grade: {data['social_studios_grade']}")
        print(f"Science Grade: {data['science_grade']}")
        print("-" * 20)
        
    input("Press any key to continue") #Presione alguna tecla para continuar


# 2.Función que se encarga de validar de que se haya ingresado información por parte del usuario
def check_if_user_information_exists(user_information):
    if not user_information:
        print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
        input("Press any key to continue") #Presione alguna tecla para continuar
        return False
    else:
        show_information_add(user_information)


'''CASE 3'''
# 1.Función que se encarga de validar si hay estudiantes suficientes
def Check_if_thereare_students(user_information):
    if not user_information:
            print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
            input("Press any key to continue") #Presione alguna tecla para continuar
            return False
    else:
        show_top_highest_average(user_information)


# 2. Determina si hay los suficientes registros para mostrar
def show_top_highest_average(user_information):
    if len(user_information) == 1:
        print("There is only one student record.") #Solo hay un registro de estudiante
    elif len(user_information) == 2:
        print("There are only two student records.") #Solo hay dos registros de estudiantes
    else:
        print("Top 3 students.") #Top 3 estudiantes
        
    calculate_top3_average_students(user_information)

# 3. Función que se encarga de validar el top 3
def calculate_top3_average_students(user_information):
    averages = {}
    
    #1. Obtener promedios
    averages = calculate_average(user_information)
    #2. Ordenar y obtiene los 3 mejores
    sorted_students = ordenate_average(averages)
    #3. Mostrar la información en pantalla
    show_ordenate_average(sorted_students)


# 4.Se encarga de generar el promedio
def calculate_average(user_information):
    averages = {}
    for name, data in user_information.items():
            total_grade = (data['spanish_grade'] + data['english_grade'] +
                            data['social_studios_grade'] + data['science_grade'] 
            )
            average = total_grade / 4
            averages[name] = average
    return averages 


# 5.Se encarga de ordenar los tres mejores promedios de mayor a menor
def ordenate_average(averages):
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]
    return  sorted_students


# 6.Muestra el resultado promedio
def show_ordenate_average(sorted_students):
    print("--- Top 3 students ---")
    for rank, (name, average) in enumerate(sorted_students, start=1):
        print(f"{rank}. {name} - Average: {average:.2f}")
    input("Press any key to continue") #Presione alguna tecla para continuar


'''CASE 4'''
# 1.Se encarga de calcular el promedio
def calculate_overall_average(user_information):
    averages = {}
    averages = calculate_average(user_information)
    return averages

# 2.Se encarga de sacar la suma de todas las notas promedio de los estudiantes
def general_average(averages):
    addition = 0
    for name, average in averages.items():
        addition += average
    return addition


# 3.Se encarga de dividir la suma entre el número de estudiantes
def division_average(addition,averages):
    overall = addition / len(averages) 
    return overall

# 4. Es la función final que se encarga de mostrar el promedio final de todos los estudiantes
def show_overall_average(user_information):
    if user_information:
        # 1. Obtenemos el diccionario de promedios
            averages_dict = calculate_overall_average(user_information)
            # 2. Sumamos los promedios
            total_sum = general_average(averages_dict)
            # 3. Calculamos la división
            overall_result = division_average(total_sum, averages_dict)
            # 4. Mostramos el resultado
            print("--- Overall Class Average ---") #Promedio General de la Clase
            print(f"The overall average of all students is: {overall_result:.2f}") #El promdio final de toda la clase es:
            input("Press any key to continue") #Presione alguna tecla para continuar
    else:
        print("No information entered. To enter data, please press option 1 or import using option 6.") #No ha ingresado información, para poder ingresar debe presionar la opción 1 o importar con la opcion 6
        input("Press any key to continue") #Presione alguna tecla para continuar


'''CASE 5'''
# 1.Está fumción se encarga de validar que hayan archivos para exportar 
def filter_export_to_csv(user_information, file_path):
    if user_information:
        export_to_csv(file_path, user_information)
        print(f"Data successfully exported!") #¡Datos exportados exitosamente!
        input("Press any key to continue") #Presione alguna tecla para continuar
    else:
        print("No current data to export.") #No hay datos actuales para exportar
        input("Press any key to continue") #Presione alguna tecla para continuar


# 2.Función se esncarga de exportar la información como archivo CSV
def export_to_csv(file_path, data):
    # Definimos los nombres de las columnas al no ser lista
    headers = ['name', 'group', 'spanish_grade', 'english_grade', 'social_studios_grade', 'science_grade']
    
    # 1. Comprobamos si el archivo ya existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # 2. Abrimos en modo append para agregar al final
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        # 3. Escribe los keys
        writer.writeheader()
        # 4. Agregamos las filas del diccionario
        for name, student_data in data.items():
            row = {'name': name}
            row.update(student_data)
            writer.writerow(row)


'''CASE 6'''
# 1.Está fumción se encarga de validar que hayan archivos para importar 
def filter_import_to_csv(file_path):
    if os.path.exists(file_path): # 1.Esta funci;on se encarga de validar en el disco duro si realmente existe un archivo en esa ruta
        data = import_to_csv(file_path)
        print("Data successfully imported!") #Datos importados con éxito
        input("Press any key to continue") #Presione alguna tecla para continuar
        return data
    else:
        print("No current data to import.") #No hay datos actuales para importar
        input("Press any key to continue") #Presione alguna tecla para continuar
        return {}


# 2.Función se esncarga de importar la información CSV como diccionario
def import_to_csv(file_path):
    all_students = {}

    try:
        # En este apartado abrimos el archivo en modo lectura
        with open(file_path, 'r', encoding='utf_8') as file:
            # 1.Dictreader convierte cada fila en diccionario
            reader = csv.DictReader(file)
            # 2. Devuelve de manera anidada
            for row in reader:
                all_students[row['name']] = {
                    'group': row['group'],
                    'spanish_grade': int(row['spanish_grade']),
                    'english_grade': int(row['english_grade']),
                    'social_studios_grade': int(row['social_studios_grade']),
                    'science_grade': int(row['science_grade'])
                }
            # 3.Retornamos la información del archivo dictreader
        return all_students 
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.") #Error: No se encontró el archivo
        return {}
    except (KeyError, ValueError):
        print("Error: The CSV file is corrupted or has an invalid format.") #Error: El archivo CSV está dañado o tiene un formato no válido
        return {}