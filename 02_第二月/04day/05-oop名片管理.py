#oop学生名片管理系统
class Student_information():#学生类
	def __init__(self,name,tel):
		self.dictionary={}
		self.name=name						#写名字
		self.tel=tel						#电话号
		self.flag=0

class Card_system():#系统类
	def __init__(self):
		self.Card_list=[]
		self.Tell_some='无发可说'
		self.flag=0
	def __str__(self):
		return '列表里的内容是'+str(self.Card_list)

	def input_list(self,x):								#行为增
		x.dictionary['name']=x.name
		x.dictionary['T.nb']=x.tel
		self.Card_list.append(x.dictionary)
		self.Tell_some='已添加'
	def Find_list(self,x):		#行为查
		for i in self.Card_list:
			if x.name == i['name']:
				self.Tell_some='以找到'
				x.flag=1
				print(i)
		if x.flag==0:
			self.Tell_some='未找到'
	def Change_list(self,x):			#行为改
		for i in self.Card_list:
			if x.name == i['name']:
				self.Tell_some='以找到'
				x.flag=1
				change_choose=input('1.修改名字2.修改电话')
				if change_choose=='1':
					name = input('输入名字')
					i['name']=name
				elif change_choose=='2':
					tel = input('输入电话号')
					i['T.nb']=tel
				else:
					print('输入错误')
				print(i)
		if x.flag==0:
			self.Tell_some='未找到'
	def Del_list(self,x):				#行为删
		for i in self.Card_list:
			if x.name == i['name']:
				self.Tell_some='以找到'
				x.flag=1
				self.Card_list.remove(i)
				self.Tell_some='已删除'
		if x.flag==0:
			self.Tell_some='未找到'
	def tell(self):					#行为说
		print(self.Tell_some)	
	def save_file(self)	
		ff=open('Student_dirfile','w')
		ff.write()
	def read_file(self)
		ff=open('Student_dirfile','r')
		ff.read()
	def cloose_file(self)
		ff.cloose()
class Menu():#菜单类
	def __init__(self,menu):
		self.m=menu
	def print_menu(self):
		while True:
			print('1.增2.查3.改4.删5.看全部6.退')
			Choose = input('输入选择:')
			if   Choose=='1':#增
				name = input('输入名字')
				tel =input('输入电话号')
				News=Student_information(name,tel)					#建信息
				Manage_student.input_list(News)		#添加
				Manage_student.tell()				#提示
			elif Choose=='2':#查
				name=input('请输入姓名')
				tel = 0
				News=Student_information(name,tel)					#建信息
				Manage_student.Find_list(News)		#查找
				Manage_student.tell()				#提示
			elif Choose=='3':
				name=input('请输入姓名')
				tel = 0
				News=Student_information(name,tel)					#建信息
				Manage_student.Change_list(News)		#查找
				Manage_student.tell()				#提示
			elif Choose=='4':
				name=input('请输入姓名')
				tel = 0
				News=Student_information(name,tel)
				Manage_student.Del_list(News)
				Manage_student.tell()
			elif Choose=='5':
				print(Manage_student)
			elif Choose=='6':
				print('已退出')
				break

Manage_student=Card_system()

m=Menu(Manage_student)

m.print_menu()

'''
			
			
			
			elif Choose=='5':
				News=Information()
'''