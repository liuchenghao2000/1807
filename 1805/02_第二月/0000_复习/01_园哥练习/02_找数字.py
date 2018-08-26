#1234组数字
'''
import random
list_1=[]
for i in range(300):
	c = (x,y,z)=(random.randint(1,4),random.randint(1,4),random.randint(1,4))
	list_1.append(c)
list_2= list(set(list_1))
for ii in list_2:
	if ii[0]==ii[1] or ii[1]==ii[2] or ii[2]==ii[0]:
		list_2.remove(ii)
print(a)
print(len(a))
'''
l_1 = [(a,b,c) for a in range(4) for b in range(4) for c in range(4)]
l_2 = list(set(l_1))
for i in l_2:
	if i[0]==i[1]:
		l_2.remove(i)
for i in l_2:
	if i[0]==i[2]:
		l_2.remove(i)
for i in l_2:
	if i[1]==i[2]:
		l_2.remove(i)
'''		
for i in l_2:
	if i[0]==i[1]:
		l_2.remove(i)
	elif i[0]==i[2]:
		l_2.remove(i)
	elif i[1]==i[2]:
		l_2.remove(i)
'''
print(l_2)
l_3=[]
for u in l_2: 
	dd = u[0]*100+u[1]*10+u[2]
	l_3.append(dd)
print(l_3)