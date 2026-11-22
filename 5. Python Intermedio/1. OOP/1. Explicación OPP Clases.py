#Python Intermedio:OOP/LAS CLASES


'''1. Creando Clases'''
#1
# Para declarar una clase usamos la palabra class seguida de su identificador.
#El standard de nombramiento de las clases en Python es PascalCase (ver Estándares de Nombramiento).
#Por ejemplo, esta es una clase vacía con el nombre Car:


class Car:
    pass

#Para crear un objeto, debemos llamar a la clase como si fuera una función que retornara ese nuevo objeto:
my_car = Car()
print(my_car)

#2
#Podemos ver que la variable my_car es un objeto o instancia de la clase Car.
#Con una sola clase puedo crear cuantas instancias yo quiera.
class Car:
    pass


my_car = Car()

my_car_2 = Car()

print(my_car)
print(my_car_2)

'''2. Atributos'''
#1
#Como mencionamos antes, un atributo es una variable dentro de un objeto.
#Tomando en cuenta que las clases son el molde de los objetos, debemos de declarar los atributos dentro de la clase.
#Así todos los objetos que se creen usando ese molde tendrán esos atributos
#Agreguemos un atributo a la clase de Car:
class Car:
	wheel_number = 4 #Atributo de 4 ruedas

#2
# Ahora podemos accesarlo una vez que instanciemos un Car.
class Car:
	wheel_number = 4


my_car = Car()
print(my_car.wheel_number)

#3 
#Al igual que con las variables, también podemos asignarle nuevos valores a los atributos.
class Car:
	wheel_number = 4


my_car = Car()
my_car.wheel_number = 6
print(my_car.wheel_number)

'''3. Métodos'''

#1 
#Como mencionamos antes, un método es una función dentro de un objeto (como el append de las listas).
#Tomando en cuenta que las clases son el molde de los objetos, debemos de declarar los métodos dentro de la clase.
#Los métodos se declaran exactamente igual que una función con la diferencia de que su primer parámetro siempre será self (más adelante veremos para qué se usa).
class Car:
	wheel_number = 4

def my_first_method(self):
	print("Hello OOP World!")
#Ahora podemos llamarlo justo como si fuera el append de una lista. Necesitamos una instancia de Car seguido de .my_first_method()
my_car = Car()
my_car.my_first_method()

#2
#Al igual que las funciones, los métodos pueden tener cuantos parámetros queramos después del self.
#Eso sí, el self es esencial y no se puede quitar ni reemplazar.
class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles and {crashes} crashes")
		
		
my_car = Car()
my_car.show_history(45000, 2)

#3
#Para qué es el self?
#Ese atributo self que tienen todos los métodos hace referencia al objeto que llame a ese método en el futuro.
#No puedo usar show_history sin tener un objeto de tipo Car.
#Así que el self en ese show_history hace referencia a ese objeto de tipo Car que usemos para llamar a show_history.
class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car()
my_car.show_history(45000, 2)

#4 
#Aquí estamos usando el self para acceder al valor del atributo wheel_number del Car que llame a ese método en el futuro.
#Y tomando en cuenta lo que vimos acá, dos objetos de tipo Car pueden tener valores de wheel_number distintos. Para eso usamos el self! Para acceder al valor del objeto específico que esté llamando al método.
class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car()

my_truck = Car()
my_truck.wheel_number = 6

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


my_car.show_history(45000, 2)
my_truck.show_history(45000, 2)
my_bigger_truck.show_history(45000, 2)

#OTRO EJEMPLO
#1
#Digamos que. siguiendo la analogía de la fábrica, Car es una fábrica que solo fabrica automóviles con motor de gasolina diesel.
#Pero también le dan la opción a sus clientes de cambiarle ese motor por uno de gasolina súper por un costo de $2000.
#Esta opción solo está disponible una vez que el automóvil está fabricado.
#Entonces podemos decir que los Car pueden tener un atributo de gas_type, y por defecto debe ser “diesel”.
class Car:
	wheel_number = 4
	gas_type = "diesel"
	
	def my_first_method(self):
		print("Hello OOP World!")
    
def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")

#Y podemos agregar un método que cambie el gas_type de “diesel” a “super” para los clientes que quieran pagar $2000 por el cambio de motor.
class Car:
	wheel_number = 4
	gas_type = "diesel"
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
	def upgrade_engine(self):
		if self.gas_type == "diesel":
			print("Cambiando el motor diesel por uno de gasolina super por $2000...")
			self.gas_type = "super"
		else:
			print("Este automovil ya tiene un motor de gasolina super!")
#Ahora podemos hacer pruebas para ver el comportamiento.
print("Primer auto")
my_car_1 = Car()
print("Auto fabricado")
print(my_car_1.gas_type)

my_car_1.upgrade_engine()

print("Auto mejorado")
print(my_car_1.gas_type)


my_car_1.upgrade_engine()

print("Segundo auto")
my_car_2 = Car()
print(my_car_2.gas_type)

'''4. Constructores'''
#1
#En la gran mayoría de los casos, no queremos que los atributos tengan un valor por defecto.
#El caso del gas_type en el ejemplo de Car es muy específico. Ahí el ”diesel” es el valor por defecto por necesidad de la fábrica. Pero en la mayoría de fábricas no es así.
#Por ejemplo, si creáramos una clase Person con un atributo de name, no querríamos que todas las personas se llamasen “Juan” apenas nacen y que luego hubiese que cambiarles el nombre
#Lo más normal sería darles un nombre único apenas nacen.
#El constructor es el método que se ejecuta por defecto cada vez que instanciamos una clase.
#Por ejemplo, cuando hacemos esto:
class Person():
	pass


person_1 = Person()\

#2
#La sentencia de person_1 = Person() está llamando el constructor de la clase Person por detrás de cámaras.
#Por defecto, todas las clases tienen un constructor vacío. No hace nada, ni requiere que le pasemos ningún parámetro.
#Sin embargo, nosotros podemos sobre-escribir ese constructor vacío añadiendo un método llamado __init__ a nuestras clases.
#En Python, todos los constructores deben llamarse __init__. No hay de otra.
class Person():
	def __init__(self):
		print("Ha nacido una persona!")


person_1 = Person()
person_2 = Person()

#3
#Desde el constructor también podemos crear atributos, como en cualquier otro método.
class Person():
	def __init__(self):
		print("Ha nacido una persona!")
		self.age = 0

person_1 = Person()
print(person_1.age)

#4
#Tambien podemos agregarle parámetros, como en cualquier otro método.
class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.age = 0

person_1 = Person("John")
print(person_1.age)

#5
#Ahora, los parámetros del constructor no se convierten automáticamente en atributos
#Son como parámetros comunes y corrientes: variables locales que dejan de existir apenas termine su scope (ver acá).

class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.age = 0

person_1 = Person("John")
print(person_1.age)
print(person_1.name)

#Si queremos que esos parámetros (que son variables comunes y corrientes) se conviertan en atributos, tenemos que guardamos como atributos. Usando el self.
class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0

person_1 = Person("John")
print(person_1.age)
print(person_1.name)

#EJEMPLO EXTRA 
#Acá un ejemplo de otra clase Car con multiples atributos que se definen desde su constructor.
class Car:
    def __init__(self, brand, line, model, color):
        self.brand = brand
        self.line = line
        self.model = model
        self.color = color


my_audi = Car("Audi", "A4", 2023, "Red")
my_bmw = Car("BMW", "X5", 2021, "Green")
my_ferrari = Car("Ferrari", "Enzo", 1999, "Red")



#EJEMPLO DE CLASE DE FOTOGRAFIAS
#También podemos usar el constructor para definir o inicializar otros atributos que no necesariamente estamos pasando como parámetros, o para definir lógica que necesitamos ejecutar al crear los objetos.
#Por ejemplo, aquí tenemos una clase de PhotographyCamera con una lista de Photos y un método para tomar fotos y agregarlas a esta lista:

class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb / 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)