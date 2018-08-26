#商品系统
print('欢迎进入——商品系统')
l = []
while True:
	print('商品操作\n \n1.添加商品\n2.查找商品\n3.更改商品\n4.删除商品\n5.退出系统')
	a = input('输入选择的值')
	if   a =='1':
		na = input('添加商品的名字')
		pl = input('添加商品的价格')
		if na =='' or pl =='':
			print('值未输入完整')
		else:
			b =[]
			b.append(na)
			b.append(pl)
			l.append(a)
	elif a =='2':
		na = input('输入查看的商品')
		for i in l:
			if na in i:
				print(i[::])
			else:
				print('无值')
	elif a =='3':
		na = input('查找商品的名字')
		for i in l:
			if na in i:
				ii = input('1.修改名字\n2.修改价格')
				if ii == '1':
					name = input('添加新名字')
					i[0]=name
				if ii == '2':
					pl = input('添加新价格')
					i[2]=pl
				print('修改完成')
			else:
				print('无值')
	elif a =='4':
		na = input('查找商品的名字')
		for i in l:
			if na in i:
				del i
				print('删除完成')
			else:
				print('无值')
	elif a =='5':
		break
	else:
		continue
