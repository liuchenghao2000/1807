import random
count=0
list =[]
while  True:
	pc = random.randint(1,100)
	list.append(pc)
	if list.count(pc)>1:	
		list.pop	
	if len(list)==10:
		break
print(list)
