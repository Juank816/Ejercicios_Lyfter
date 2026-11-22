#Ejercicios de OOP: Clase Bus
'''Cree una clase de Bus con:
Un atributo de max_passengers.
Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase 
Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar 
un mensaje de que el bus está lleno.
Un método para bajar pasajeros uno por uno (en cualquier orden).'''

class Bus:
    

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.bus_list = []


    def add_passenger(self, person):
        if len(self.bus_list) < self.max_passengers:
            print(f"Pasajero {person.name} ingresó al bus!")
            self.bus_list.append(person.name)
        else:
            print("Lo siento, el bus está lleno")

    def bus_stop(self, person):
        print(f"Pasajero {person.name} tocó el timbre para bajar!")
        self.bus_list.remove(person.name)


class Person:
    def __init__(self, name):
        print(f"El pasajero con nombre {name}!")
        self.name = name
        self.counter_person = 1


#Creamos el bus
bus1 = Bus(3)

#Creamos a las personas
person_1 = Person("Ana")
person_2 = Person("Luis")
person_3 = Person("Melany")

#Agregamos a las personas al bus
bus1.add_passenger(person_1)
bus1.add_passenger(person_2)
bus1.add_passenger(person_3)

#Imprimimos las personas que van en el bus
print(bus1.bus_list)

#Pasajero person 1 decide bajarse\
bus1.bus_stop(person_1)

#Imprimimos las personas que van en el bus
print(bus1.bus_list)

