#Manejo de Archivos: Primer ejemplo de como se utiliza WHIT y manejo de Archivos

import os

print(os.getcwd()) 
print(os.path.exists('quijote.txt'))

#with open(r'D:\Curso Lyfter\MÓDULOS\4. Python Básico\29. Manejo de Archivos\quijote1.txt', 'r') as file: //Esta línea fue porque no me encontraba el archivo 

with open(r'MÓDULOS/4. Python Básico\29. Manejo de Archivos\quijote1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)