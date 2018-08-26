#列表	[]推导式子变()	列表生成器
#函数	yield			函数变生成器

#l = (x for x in range(90) if x%10==0 and x!=20)
#print(next(l))
#print(next(l))
#print(next(l))
#斐波拉切数
def func(number):
	a,b=0,1
	for i in range(number):
		#print(b)
		sy = yield b
		a,b=b,a+b
		print(sy)
		print('----')
test=func(10)

test.send(None)
test.send('N')
test.send(' o')
test.send('  n')
test.send('   e')

for i in test:
	pass