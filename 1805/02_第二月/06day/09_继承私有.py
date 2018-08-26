#继承私有

class A_test():
	def __init__(self):
		self.__money=1000000
	def get_money(self):
		return self.__money
class B_test(A_test):
	pass

b=B_test()
c = b.get_money()
print(c)
