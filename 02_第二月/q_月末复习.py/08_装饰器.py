#装饰器
def w(x):
	if x==1:
		def inner(fun):
			fun()
			print('验证成功')
	elif x==2:
		def inner(fun):
			fun()
			print('验证成功')
			return 
	return inner

@w(1)
def game():
	print('王者农药')

@w(2)
def game():
	print('你是药神')

