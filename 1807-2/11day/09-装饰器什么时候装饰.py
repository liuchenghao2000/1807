def w1(fun):
	print('哈哈哈哈哈')
	def inner():
		print('呵呵呵呵呵呵')
		print('检查登录')
		fun()
	return inner

@w1#相当于pay = w1(pay)  语法糖
def pay():
	print('支付中')


pay()#此时装饰器已经装饰完毕