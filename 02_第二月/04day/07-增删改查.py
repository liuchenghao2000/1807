#学生管理系统
all__student=[]
while True:
	choose = input('输入选项\n1.增加2.查找3.改变4.删除5.退出')
	flag= 0
	if choose =='1':
		name   = input('请输入姓名')
		ID_nub = input('请输入ID号')
		new_information={}
		new_information['name']=name
		new_information['ID_nb']=ID_nub
		all__student.append(new_information)
		print('已添加')
	elif choose=='2':
		name   = input('请输入姓名')
		for i in all__student:
			if i['name'] == name:
				print('已找到')
				flag= 1
				print(i)
		if flag==0:
			print('未找到')
	elif choose=='3':
		name   = input('请输入姓名')
		for i in all__student:
			if i['name']==name:
				print('已找到')
				flag= 1
				choose=input('1.更改姓名2.更改ID号')
				if choose=='1':
					i['name']=input('输入名字')
				elif choose=='2':
					i['ID_nb']=input('输入ID号')
		if flag==0:
			print('未找到')
	elif choose=='4':
		name   = input('请输入姓名')
		for i in all__student:
			if i['name']==name:
				print('已找到')
				all__student.remove(i)
				print('已删除')
		if flag==0:
			print('未找到')
	elif choose=='5':
		break
	print('-'.center(20,' '))
