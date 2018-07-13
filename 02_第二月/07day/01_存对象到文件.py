#存对象到文件
class objectsome():
	def __init__(self):
		self.Thatlist=[]
	def save_file(self,x):
		name = input('输入打开或者新建的文件名')
		self.f_1=open(name,'a+')
		self.f_1.write(str(x))
	def read_file(self):
		name = input('输入打开读取的文件名')
		self.f_1=open(name,'r')
		self.f_1.read()
	def copy_file(self):
		name = input('输入需要拷贝的文件')
		self.f_1=open(name,'r')
		cc = name.rfind('.')
		self.f_2=open(name[0:cc]+'_copy'+name[cc:],'w')
		ccc =self.f_1.read()
		self.f_2.write(ccc)
		self.f_1.close()
		self.f_2.close()
	def open_file(self):
		name = input('输入需要打开查看的文件')
		self.f_1=open(name,'r')
		sinf = self.f_1.read()
		abc = eval(sinf)
		aac = type(abc)
		return  aac
	def close_file(self):
		self.f_1.close()

class some_information():
	def __init__(self,A,B):
		self.information=(A,B)
while True:
	alll_inf=objectsome()
	A = input('输入A的内容')
	B = input('输入B的内容')
	if A=='3':
		break
	part_inf=some_information(A,B)

	alll_inf.save_file(part_inf.information)
	#alll_inf.read_file()
	#alll_inf.copy_file()
	alll_inf.open_file()
	alll_inf.close_file()
print(aac)
#eval