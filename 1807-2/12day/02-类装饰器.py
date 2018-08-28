class Dog():
	def __init__(self,fun):
		self.fun = fun

	def __call__(self):
		print('验证')
		self.fun()

'''
dog = Dog('xxx')
print(dog)#__str__
dog()#__call__
'''


@Dog
def test():
	print('哈哈哈')


#dog = Dog(test)
#dog()#call
test()