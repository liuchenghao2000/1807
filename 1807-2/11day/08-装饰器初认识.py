def w1(fun):
	def inner():
		print('检查登录')
		fun()
	return inner

def pay():
	print('支付中')



pay = w1(pay)
pay()