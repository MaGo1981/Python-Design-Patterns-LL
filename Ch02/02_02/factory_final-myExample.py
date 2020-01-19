from datetime import datetime

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
	# print(menu)

	return menu[food]

m = addMealToCard("mushrooms")
h = addMealToCard("ham")
o = addMealToCard("olives")
s = addMealToCard("sicilianPizza")

# print(m)
# print(h)
m.setSpecialInstructions("Crazy mushrooms.")
o.setSpecialInstructions("Only black olives.")
# print(m)
# print(o)
s.setTopping1(h)
s.setTopping2(m)
s.setTopping3(o)
s.setSpecialInstructions("Three toppings all over the pizza")
# print(s)

class FoodPrice():
	def __init__(self, name, smallRegular, largeRegular):
		self._name = name
		self._smallRegular = smallRegular
		self._largeRegular = largeRegular


	def __str__(self):
		return str(self._name) + '\n '


class PizzaPrice(FoodPrice):
	def __init__(self, name, smallRegular, largeRegular, small1topping, large1topping,\
	small2toppings, large2toppings, small3toppings, large3toppings, smallSpecial, largeSpecial):
		FoodPrice.__init__(self, name, smallRegular, largeRegular)
		self._small1topping = small1topping
		self._large1topping = large1topping
		self._small2toppings = small2toppings
		self._large2toppings = large2toppings
		self._small3toppings = small3toppings
		self._large3toppings = large3toppings
		self._smallSpecial = smallSpecial
		self._largeSpecial = largeSpecial




class Item():
	def __init__(self, food=s, size="small", quantity=3):
		self._food = food
		self._size = size
		self._quantity = quantity
		self._price = None
		self._total = None



	def setPizzaItemPriceAndTotal(self, pizzaPrice):
		if self._size == 'large' and self._food._specialInstructions != None:
			self._price = pizzaPrice._largeSpecial
		elif self._size == 'small' and self._food._specialInstructions != None:
			self._price = pizzaPrice._smallSpecial
		elif self._size == 'large' and self._food._topping3 != None:
			self._price = pizzaPrice._large3toppings
		elif self._size == 'small' and self._food._topping3 != None:
			self._price = pizzaPrice._small3toppings
		elif self._size == 'large' and self._food._topping2 != None:
			self._price = pizzaPrice._large2toppings
		elif self._size == 'small' and self._food._topping2 != None:
			self._price = pizzaPrice._small2toppings
		elif self._size == 'large' and self._food._topping1 != None:
			self._price = pizzaPrice._large1toppings
		elif self._size == 'small' and self._food._topping1 != None:
			self._price = pizzaPrice._small1toppings
		elif self._size == 'large' and self._food._topping1 == None:
			self._price = pizzaPrice._largeRegular
		else:
			self._price = pizzaPrice._smallRegular
		self._total = self._price*self._quantity

	def setItemPriceAndTotal(self, itemPrice):
		if self._size == 'large':
			self._price = itemPrice._largeRegular
		elif self._size == 'small':
			self._price = itemPrice._smallRegular
		self._total = self._price*self._quantity


	def __str__(self):
		return str(self._food) + '\nsize: ' + str(self._size) + ',\nquantity: ' + str(self._quantity) +  ',\nprice: ' + str(self._price) +  ',\ntotal: ' + str(self._total) +  '\n________________\n'

i1 = Item()
p1 = PizzaPrice(i1._food._name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i1.setPizzaItemPriceAndTotal(p1)

i2 = Item(food=o, size="small")
p2 = FoodPrice(i2._food._name, 1, 2)
i2.setItemPriceAndTotal(p2)

i3 = Item(size="large")
p3 = PizzaPrice(i3._food._name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i3.setPizzaItemPriceAndTotal(p3)

# print(p1)
# print(i1._price)
# print(p2)
# print(i2._price)
# print(p3)
# print(i3._price)

lista = [i1, i2, i3]

class Order():
	def __init__(self, lista, user=1):
		self._items = lista
		self._user = 'Marko'
		self._created = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #models.DateTimeField(auto_now_add=True)

	def getItems(self):
		return self._items

	def getUser(self):
		return "User:" + self._user

	def getDT(self):
		return "Date & Time:" + self._created


	def __str__(self):
	    return str(self.getUser()) + '\n\n' + '\n'.join(map(str, self._items)) + '\n\n' + self.getDT()
		# return elements from a list of objects  - '\n'.join(map(str, self._items))

order = Order(lista)
print(order)
