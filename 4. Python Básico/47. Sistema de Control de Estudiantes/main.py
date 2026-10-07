#TRABAJO FINAL PYTHON BÁSICO: Sistema de Control de Estudiantes
'''Requerimientos 📋
1.Deberá validar que se ingrese una opción válida del menú.
2.Ingresar información de n cantidad de estudiantes, uno por uno. Cada estudiante debe incluir:
Nombre completo
Sección (ejemplo: 11B)
Nota de español
Nota de inglés
Nota de sociales
Nota de ciencias
3.Deberá validar que las notas ingresadas sean válidas (números de 0 a 100) y 
seguir pidiéndolas hasta que sean válidas.
4. Ver la información de todos los estudiantes ingresados.
5. Ver el top 3 de los estudiantes con la mejor nota promedio 
(es decir, el promedio de nota de español + nota de inglés + nota de sociales + nota de ciencias).
6.Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio de notas de cada uno).
7.Exportar todos los datos actuales a un archivo CSV.
8.Importar los datos de un archivo CSV previamente exportado. Si no hay un archivo previamente exportado, debe informárselo al usuario.'''

#Importaciones de otros módulos
from menu.menu import menu


# 1. La función principal del main ejecutable
def main(): # Tenemos la función main principal
    try :
        menu() 
    except Exception as ex:
        print("An unexpected error ocurred: {ex}")

if __name__ == "__main__":
    main() 