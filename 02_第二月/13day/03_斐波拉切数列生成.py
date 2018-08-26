def fib(num):
	a,b = 0,1			#1
	for i in range(num):
		print(b)		#2
		temp=yield a
		a,b =b,a+b		#3
		print(temp)
g = fib(8)


next(g)
g.send('帅')
g.send('帅')
g.send('帅')
g.send('帅')
g.send('帅')
g.send('帅')
g.send('8帅')