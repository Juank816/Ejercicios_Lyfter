#Ejercicios de Sintaxis: DADA CIERTA CANTIDAD DE NOTAS CALCULAR
'''Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.''' 

print ("---- Analiza Notas de Estudiantes ----")

#Declaración de variables
#////////////////////////////////////////////////
total_grades = float
counter_grades = int
passing_grades = int
actual_grade = float
failing_grades = int
average_passing_grades = float
average_failed_grades = float
overall_average_grade = float
total_grades = 0
counter_grades = 1
passing_grades = 0
actual_grade = 0
failing_grades = 0
average_passing_grades = 0
average_failed_grades = 0
overall_average_grade = 0

# Pedir información al usuario
total_grades = int(input("Ingrese la cantidad de notas "))

#Ciclos
while counter_grades <= total_grades:
    actual_grade = float(input(f"Ingrese la nota número {counter_grades} "))
    if actual_grade < 70:
        failing_grades = failing_grades + 1
        average_failed_grades = average_failed_grades + actual_grade
    else:
        passing_grades = passing_grades + 1
        average_passing_grades = average_passing_grades + actual_grade
    
    overall_average_grade = overall_average_grade + (actual_grade / total_grades)
    counter_grades = counter_grades + 1

#Cálculos finales de los promedios
if passing_grades > 0:
    average_passing_grades = average_passing_grades / passing_grades
if failing_grades > 0:
    average_failed_grades = average_failed_grades / failing_grades

#Mostrar en pantalla
print(f"El estudiante cuenta con un total de {passing_grades} aprobadas")
print(f"Con promedio de {average_passing_grades} aprobadas")

print(f"El estudiante cuenta con un total de {failing_grades} desaprobadas")
print(f"Con promedio de {average_failed_grades} desaprobadas")
print(f"El promedio total de las notas es de {overall_average_grade}")

