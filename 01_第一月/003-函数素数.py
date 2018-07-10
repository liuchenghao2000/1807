#函数声明

def su(a,b):
	lis=[]
	for i in range(a,b):
		f=0
		for u in range(2,i):
			if i%u==0:
				f=1
				break
		if f==0:
			lis.append(i)
	return lis 

#函数调用
ss =su(50,100)
print(ss)
