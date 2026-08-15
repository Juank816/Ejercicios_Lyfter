#Ejercicios extra de Iterables y Listas: PIDE Y MUESTRA LAS PALABRAS MAYORES A 4 LETRAS
'''Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con 
solo aquellas palabras que tengan más de 4 letras'''

print("---- Muestra solo Palabaras Ingresadas Mayor a 4 Letras  ----")

#Declaración de lista
my_list = []
new_list = []

#Declaración de variables
strings = str
strings = ""


#Pedirle información al usuario
print("Por favor ingrese 5 palabras.")
for index in range(0, 5):
    strings = input(f"Ingrese la #{index + 1} palabra a la lista: ")
    my_list.append(strings)

#Analiza las palabras con más de 4 letras
for index in range(0, len(my_list)):
    if len(my_list[index]) > 4:
        new_list.append(my_list[index])


#Imprime en pantalla la nueva lista 
print(new_list)