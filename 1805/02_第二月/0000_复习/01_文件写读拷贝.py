#文件写读拷贝

class File_do_somting():
	def __init__(self):
		self.name=input('输入文件名')+'.txt'
	def New_file(self):			#新文件
		f=open(self.name,'w')
		Aw=input('请写一些东西')
		f.write(Aw)
		f.close()
	def write_file(self):		#追加
		f=open(self.name,'a+')
		self.Aw=input('请写一些东西')
		f.write(self.Aw)
		f.close()
	def read_file(self):		#读文件
		f=open(self.name,'r')
		self.Aw=f.read()
		print(self.Aw)
		f.close()
	def copy_file(self):		#拷贝
		nub = self.name.rfind('.')
		self.read_file()
		self.name=self.name[0:nub]+'_copy'+self.name[nub:]
		self.write_file()

A_file=File_do_somting()
A_file.name
A_file.New_file()
A_file.write_file()
A_file.read_file()
A_file.copy_file()
