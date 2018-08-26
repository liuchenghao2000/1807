def func(i):
	if i>=1:
		x= i*func(i-1)
		print(x)4
	else:
		x=1
	return x 

print(func(10))


