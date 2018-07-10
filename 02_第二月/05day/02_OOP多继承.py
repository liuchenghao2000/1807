#多继承

class A():
	def __init__(self):
		self.name='wang'
		self.__habit='爱运动'

		print('2')
	def shadow(self):
		return self.__habit
class B():
	def __init__(self):
		self.name='song'
		self.__habit='爱音乐'
		print('1')
	def shadow(self):
		return self.__habit

class C(B,A):
	pass

c=C()
print(c.name)
print(c.shadow())