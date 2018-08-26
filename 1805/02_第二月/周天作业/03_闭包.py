#方程

def func(a, b):
	def inner(x):
		return a*x+b
	return inner


test = func(3, 4)
test = test(4)
print(test)