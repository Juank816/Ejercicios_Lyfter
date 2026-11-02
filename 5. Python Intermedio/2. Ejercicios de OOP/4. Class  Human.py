#Ejercicios de OOP: Clase Human
'''Cree las siguientes clases:
Head
Torso
Arm
Hand
Leg
Feet
Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.'''

class Human:
	def __init__(self, torso):
            self.torso = torso

class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		self.right_leg = right_leg
		self.left_leg = left_leg


class Head:
	def __init__(self):
            pass

class Hand:
	def __init__(self):
		pass

class Arm:
	def __init__(self, hand):
		self.hand = hand

class Leg:
	def __init__(self,feet):
            self.feet = feet

class Feet:
	def __init__(self):
            pass

head = Head()
right_hand = Hand()
left_hand = Hand()
right_feet = Feet()
left_feet = Feet()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

person = Human(torso)

print(isinstance(person.torso.right_arm.hand, Hand))