def w1(fun):
	def inner():
		print('检查登录')
		return inner
	return inner

@w1
def pay():
	print('支付中')
	return '老王'

ret = pay()
print(ret)