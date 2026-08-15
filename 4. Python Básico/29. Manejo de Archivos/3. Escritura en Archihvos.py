#Manejo de Archivos:Escritura de Archivos ✍🏻

def write_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

new_text = "Capítulo II. Que trata de la primera salida que de su tierra hizo el ingenioso Don Quijote."

print(write_new_file(r'MÓDULOS/4. Python Básico\29. Manejo de Archivos\quijote1.txt', new_text))