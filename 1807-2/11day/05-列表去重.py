list2 = [1,2,3,3]
list1 = []
for i in list2:
	if i not in list1:
		list1.append(i)
print(list1)
print(list(set(list2)))