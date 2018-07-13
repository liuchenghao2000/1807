#公有/私有，属性/方法 使用
class A_test():
	def __init__(self):
		self.__name='超帅'
	def __sometest(self):
		return self.__name
#		return 'haha'
	def getname(self):
#		return self.__name
		return self.__sometest()
a = A_test()
c = a.getname()
#print(a.__name)	
print(c)
