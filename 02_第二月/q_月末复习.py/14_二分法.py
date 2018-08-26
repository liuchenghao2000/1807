#二分法	必须有序		找数索引
'''
arr=[312,3123,3123,1231,41,5,2757,558607,80,87423,46,57]
arr.sort()
key = int(input('请输入查找的数字'))
min = 0
max = len(arr)-1
center = int((min + max)/2)
if key in arr:
	while True:
		#key 在数组左
		if arr[center] > key:
			center = center -1
		#key 在数组右
		elif arr[center] < key:
			center = center +1
		#找到了
		elif arr[center] == key:
			print(str(key)+'在数组'+str(center)+'个位置')
			break
else:
	print('没有该数字')
'''
arr=[312,3123,3123,1231,41,5,2757,558607,80,87423,46,57]
arr.sort()
#print(arr)
key = int(input('请输入查找的数据'))#5
min = 0
max = len(arr)-1
center = int((min + max)/2)
if key in arr:
	while True:
		if arr[center]>key:
			center=center-1
		elif arr[center]<key:
			center=center+1
		elif arr[center]==key:
			print(str(key)+'在数据'+str(center))
			break
else:
	print('未找到该数据')
