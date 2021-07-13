
import copy

class Prototype:

	def __init__(self):
		self._objects = {}
	
	def register_object(self, name, obj):
		self._objects[name] = obj
	
	def unregister_object(self, name):
		del self._objects[name]
	
	def clone(self, name, **attr):
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj
		
	
class Car:
	def __init__(self):
		self.name = "Ford"
		self.color = "blue"
	
	def __str__(self):
		return f"{self.name} {self.color}"
		

c = Car()

prototype = Prototype()
prototype.register_object("Ford", c)

## c1 is now a clone of the Car object with the name Ford BUT with color red!
c1 = prototype.clone(c.name, color="red")

print(c1)
