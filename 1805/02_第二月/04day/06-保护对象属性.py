class father():
	def __init__(self):
		self.__count=3
	def a(self):
		return self.__count

	def __b(self):
		return 40
	def xxxx(self):
		return self.__b()

f=father()
print(f.a())
print(f.xxxx())