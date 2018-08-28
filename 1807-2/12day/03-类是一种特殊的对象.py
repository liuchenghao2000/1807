def choose(type):
	if type == 1:
		class Dog():
			pass
		return Dog

	else:
		class Cat():
			pass
		return Cat

Dog = choose(1)
dog = Dog()		