#Os系统模块使用
import os
class Use_Os():
	#文件操作
	def Open_file(self):
		name=input('输入新建文件名')
		file=open(name,'w')
		file.close()
	def Os_Nname(self):		#更名
		old_n=input('要更改的文件名')
		if old_n in os.listdir('./'):
			new_n=input('新名字')
			os.rename(old_n,new_n)
		else:
			print('无此文件')
	def Os_Remove(self):	#删
		A_file=input('输入删除的文件名')
		if A_file in os.listdir('./'):
			a = input('y/n')
			if a =='y':
				os.remove(A_file)
		else:
			print('找不到要删除的文件')
	#文件夹操作
	def Os_Mkdir(self):		#新建文件夹
		a = input('输入文件夹名字')
		if a not in os.getcwd():
			os.mkdir(a)
		else:
			print('已存在')
	def Os_Now_dir(self):	#显示当前目录路径 #文件夹进出操作多用
		aa = os.getcwd()
		print(aa)
	def Os_Chdir(self):		#改变默认目录
		aa=os.chdir('文件夹名字') 	#进入是文件夹名字	#出是 ..
		print(aa)
	def Os_get_list(self):	#获取目录 列表(呈现方式)	#文件操作多用
		aa=os.listdir('./')
		print(aa)
	def Os_Del_f(self):	#删除文件夹
		a = input('输入删除文件夹的名字')
		if a in os.getcwd():
			os.rmdir(a)
			print('以删除')
		else:
			print('此文件夹无此')
'''
	def Os_Def_files(self):
		import shutil
		shutil.rmtree('xxx文件夹')
'''
ABC_file=Use_Os()
'''
ABC_file.Open_file()
ABC_file.Os_Nname()
ABC_file.Os_Remove()
'''

ABC_file.Os_Mkdir()
ABC_file.Os_Now_dir()
#ABC_file.Os_Chdir()
ABC_file.Os_get_list()
ABC_file.Os_Del_f()

