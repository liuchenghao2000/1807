
import random
list1=[]
def numberx():
	global list1
	while True:
		num=random.randint(1,100)
		if len(list1)==10:
			print('添加完成')
			print('----------')
			break
		if num in list1:
			continue
		list1.append(num)
  
	print(list1)
	mark=list1[7]
	print('标记7是%d\n重新排序'%mark)
	list1.sort()
	print(list1)
	for inx,val in enumerate(list1):
		if mark==val:
			print('索引是%d'%inx)
			print('数字是%d'%val)
			break

numberx()