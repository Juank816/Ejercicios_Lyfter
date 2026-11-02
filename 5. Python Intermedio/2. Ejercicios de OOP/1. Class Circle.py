#Ejercicios de OOP: Clase Circle
'''Cree una clase de Circle con:
Un atributo de radius (radio).
Un método de get_area que retorne su área.'''


class Circle:
    radius = 3

    def get_area(self):
            r = self.radius ** 2    
            area = r * 3.14
            return area

circle1 = Circle()
print(f"El área del circulo es: {circle1.get_area()}")  