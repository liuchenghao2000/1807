def w1(fun):
	def inner(*args,**kwargs):
		print('装饰中')
		return fun(*args,**kwargs)
	return inner

@w1
def show1():
	print('哈哈哈')

@w1
def show2(arg):
	print('哈哈哈哈')
	print(arg)

@w1
def show3():
	print('哈哈哈哈哈')
	return '呵呵呵呵'

@w1
def show4(arg):
	print('哈哈哈哈哈哈哈哈')
	return arg

	
ret = show4('老王')
print(ret)