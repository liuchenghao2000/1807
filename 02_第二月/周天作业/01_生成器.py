'''
#生成器
def fib(a,b):
	def inner(x):
		return a*x+b
	return inner
cc = fib(0,1)
dd = cc(9)
print(dd)
'''
import time
#斐波拉切生成器
def fibla(a,b):
	while True:
		#print(b)
		time.sleep(1)
		#yield a
		tem = yield b
		print(tem)
		a, b = b, a+b
test=fibla(0,1)
'''
test.send(None)
print('-------')
test.send('卡了一下')
print('-------')
test.send('卡了一下')
print('-------')
'''
for i in test:
	#print(next(test))
	test.send('卡了一下')
	print('-------')
