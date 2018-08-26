list_1=[x for x in range(1,10)]+[123]

num = 100
flag=0
#-----1-----
for i in list_1:
	if num==list[i]:
		print(i)
		flag=1
#...1...
if flag==1:
	print('无文件')
#...2...
if list_1.count(num)==0:
	print('无文件')
print(list_1)

#-----2-----
a =list_1.find(num)
if a==0:
	print('无信息')
else：
	print(a)

