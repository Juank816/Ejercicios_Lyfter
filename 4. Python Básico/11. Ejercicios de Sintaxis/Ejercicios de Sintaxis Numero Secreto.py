#Ejercicios de Sintaxis: NÚMERO SECRETO
'''Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario 
adivine el numero.'''

#Importaciones de librería externas
import random

print("---- Generador de Número Secreto ----")

#Declaración de variables
#////////////////////////////////////////////////
user_number = int
user_number = 0
number = random.randint(1,10)
user_number = int(input("Ingrese un número: "))


#PROCESO
#////////////////////////////////////////////////
while number != user_number:
    user_number = int(input("¡No ha adivinado el número secreto!. Ingrese nuevamente un número "))
    
print("¡Lograste adivinar el número secreto!")