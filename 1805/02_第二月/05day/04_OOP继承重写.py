#继承重写

class Animal(object):
	def __init__(self, arg):
		self.arg = arg

class Dog(object):
	def __init__(self, arg):
		super(Dog, self).__init__()
		self.arg = arg
		
class Adog(object):
	def __init__(self, name):
		super(Adog, self).__init__(Dog)
		self.arg = arg
						
TellSkyDog=Animal()						
