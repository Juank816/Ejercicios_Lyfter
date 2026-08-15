#Ejercicios de Funciones: RETORNA UN STRING CON PALABRAS SEPARADAS
'''Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero
ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable””'''

#Funciones
def ordenate_string(my_string):
    #Lista
    my_list = []
    #Variables de función
    result = ""
    
    my_list = my_string.split("-")
    my_list.sort()
    result = "-".join(my_list)
    return result 


def main():
    print("---- Programa que muestra cuántas mayúsculas y minúsculas tiene un string ----")
    my_string = "python-variable-funcion-computadora-monitor"
    print(ordenate_string(my_string))


if __name__ == "__main__":
    main()