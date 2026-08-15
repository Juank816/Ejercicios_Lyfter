#Ejercicios extra de Excepciones: Función que suma los valores de una lista 
''' Cree una función sumar_valores(lista) que:
Reciba una lista de elementos (strings, enteros, flotantes mezclados)
Intente convertir cada elemento a tipo float
Si puede, sume el valor y muestre: "<valor> sumado correctamente"
Si no puede, muestre: "Elemento inválido: <valor>"
Al final, imprima la suma total'''

def sum_values(my_list):
    addition = 0
    for index in my_list:
        try:
            number = float(index)
            print(f"{number} sumado correctamente ")
        except ValueError:
            print(f"Elemento inválido: {index}")
    print(f"Total de la suma: {addition}")


def main():
    
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    #Se llaman a las funcion
    sum_values(my_list)


if __name__ == "__main__":
    main()