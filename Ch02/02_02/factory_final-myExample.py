class Food():
	"""A simple food class"""

	def __init__(self, name):
		self._name = name
		self._specialInstructions = None

	def setSpecialInstructions(self,specialInstructions):
		self._specialInstructions = specialInstructions

class Topping(Food):
	"""A simple topping class"""

	def __init__(self, name="Ham", side="Right"):
		Food.__init__(self, name)
		self._side = side



	def __str__(self):
		if self._specialInstructions != None:
			return str(self._name) + ',\nside: ' + str(self._side)  + ',\nspecial instructions: ' + str(self._specialInstructions) + '\n '
		else:
			return str(self._name) + ',\nside: ' + str(self._side) + '\n '



class Pizza(Food):
	"""A simple pizza class"""

	def __init__(self, name="Sicilian Pizza"):
		Food.__init__(self, name)
		self._topping1 = None
		self._topping2 = None
		self._topping3 = None

	def setTopping1(self,topping1):
		self._topping1 = topping1

	def setTopping2(self,topping2):
		self._topping2 = topping2

	def setTopping3(self,topping3):
		self._topping3 = topping3

	def __str__(self):
		if self._topping1 != None and self._specialInstructions != None and self._topping2 == None and self._topping3 == None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name) \
			+ ',\nspecial instructions: ' + str(self._specialInstructions) + '\n '
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 == None and self._topping3 == None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name)
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 != None and self._topping3 == None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name) + ',\ntopping2: ' + str(self._topping2._name)
		elif self._topping1 != None and self._specialInstructions != None and self._topping2 != None and self._topping3 == None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name) + ',\ntopping2: ' + str(self._topping2._name)\
			+ ',\nspecial instructions: ' + str(self._specialInstructions) + '\n '
		elif self._topping1 != None and self._specialInstructions == None and self._topping2 != None and self._topping3 != None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name) + ',\ntopping2: ' + str(self._topping2._name)\
			 + ',\ntopping3: ' + str(self._topping3._name)
		elif self._topping1 != None and self._specialInstructions != None and self._topping2 != None and self._topping3 != None:
			return str(self._name) + ',\ntopping1: ' + str(self._topping1._name) + ',\ntopping2: ' + str(self._topping2._name)\
			+ ',\ntopping3: ' + str(self._topping3._name) + ',\nspecial instructions: ' + str(self._specialInstructions) + '\n '
		else:
			return str(self._name) +'\n '



def addMealToCard(food='mushrooms'):
	"""The factory method"""

	menu = dict(mushrooms=Topping("Mushrooms", "Left"), ham=Topping(), olives=Topping("Olives", "Whole"), sicilianPizza=Pizza())

	return menu[food]

m = addMealToCard("mushrooms")
h = addMealToCard("ham")
o = addMealToCard("olives")
s = addMealToCard("sicilianPizza")

# print(m)
print(h)
m.setSpecialInstructions("Crazy mushrooms.")
o.setSpecialInstructions("Only black olives.")
print(m)
print(o)
s.setTopping1(h)
s.setTopping2(m)
s.setTopping3(o)
s.setSpecialInstructions("Three toppings all over the pizza")
print(s)
