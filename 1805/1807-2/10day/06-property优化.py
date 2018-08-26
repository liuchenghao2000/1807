class Dog():
	def __init__(self):
			self.__age = 100

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,age):
		self.__age = age

dog = Dog()
#dog.setAge(150)
#print(dog.getAge)

dog.age = 900
print(dog.age)
#print(dog.getAge())
