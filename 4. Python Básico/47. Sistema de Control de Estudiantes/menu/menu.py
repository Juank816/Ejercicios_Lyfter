#PROYECTO: Sistema de Control de Estudiantes
'''Importaciones'''
from actions.actions import give_number_students, give_information_students,check_if_user_information_exists,Check_if_thereare_students
from actions.actions import show_overall_average, filter_export_to_csv, filter_import_to_csv
'''Menú principal del programa.'''

# 1.Función del menú
def menu():
    result_information = {}
    while True:
        print(
            "1. Enter student information\n"                    # 1. Ingresar información de estudiantes
            "2. View added student information\n"               # 2. Ver información de los estudiantes ingresados
            "3. View students with the highest average grade\n" # 3. Ver estudiantes con la mejor nota promedio
            "4. View the average grade of all students\n"       # 4. Ver la nota promedio de todos los estudiantes
            "5. Export all current data to a CSV file\n"        # 5. Exportar todos los datos actuales a un archivo CSV  
            "6. Import all data from a CSV file\n"              # 6. Importar todos los datos de un archivo CSV
            "7. Exit\n"                                         # 7. Salir 
        )
        try:
            option = int(input("Please enter the number of the option you wish to perform: ")) # Por favor ingresa el número de la opción que desea realizar:
            match option:
                case 1: 
                    number_students_main = give_number_students() # 1.Solicita el número de estudiantes a agregar
                    result_information = give_information_students(number_students_main) # 2. Recopila la informción ingresada por el usuario
                case 2:
                    check_if_user_information_exists(result_information) # 1.Función que se encarga de validar de que se haya ingresado información por parte del usuario y mostrarla
                case 3:
                    Check_if_thereare_students(result_information) # 1.Función que se encarga de validar si hay estudiantes suficientes y calacular el top 3 estudiantes
                case 4:
                    show_overall_average(result_information) # 1. Es la función final que se encarga de mostrar el promedio final de todos los estudiantes
                case 5:
                    filter_export_to_csv(result_information, 'data/students.csv') # 1.Función se esncarga de exportar la información como archivo CSV
                case 6:
                    result_information = filter_import_to_csv('data/students.csv') # 1.Función se esncarga de importar la información CSV como diccionario
                case 7:
                    print("Exiting...") # 1.Está opción se encarga de sacarnos del programa
                    break
                case _:
                    print("Invalid option. Please enter a valid option.") #Opción no valida. Por favor ingrese una opción válida
        except ValueError:
            print("An error occurred; no valid option was selected.") #Ha ocurrido un error, no se ha selccionado ninguna opción valida.
