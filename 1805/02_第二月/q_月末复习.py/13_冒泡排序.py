l=[2,4,8,9,1,35,512,23523,242342,12313,14124,121,231,231,4124,12,33,1]
l=list(set(l))
print(l)
print('-------------')
#数据比较，大数后排
#for i in range(len(l)):
#	for j in range(i+1,len(l)):
#		if l[i]>l[j]:
#			l[i],l[j]= l[j],l[i]
#	print(l)
#print('-------------')
#print(l)


for i in range(len(l)):
	for u in range(i+1,len(l)):
		if l[i]>l[u]:
			l[i],l[u]=l[u],l[i]#u前移动
print(l)