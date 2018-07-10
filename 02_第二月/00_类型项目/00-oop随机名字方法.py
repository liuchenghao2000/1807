import random
class Liebiao_Number():
	def __init__(self):
		self.Number_list=[]
	def Add(self,x):
		if x not in self.Number_list:
			self.Number_list.append(x.number)
		else:
			pass
	def read(self):
		print(self.Number_list)
class Random_Number():
	def __init__(self,First_number,End_number):
		self.number=random.randint(First_number,End_number)

class all_Name():
	def __init__(self):
		self.name_list=['于亮','李宜航','靳彦昆','邢凯','贾梦豪','马宇星','尹天','常瑞贤','张浩楠','郑涵策','董帅','王学文','邵广超','白冰','王伟录','周肸','王晓俊','张世豪','曹宗亮',
'赵伟奇','吴玉泽','王哲','张伟','柴子健','李宁','李爽','崔睿']

class File_system():
	def __init__(self,file_txt):
		self.file=open(file_txt,'a+')
	def write_file(self,x):
		self.file.write(x)
	def cloose_file(self):
		self.file.cloose()

R_Number_list=Liebiao_Number()
Al_Name=all_Name()

file_name1=File_system('001_random_name_test.txt')

print(len(Al_Name.name_list),'人')
while True:
	ABC=Random_Number(0,26)
	R_Number_list.Add(ABC)
	if len(R_Number_list.Number_list)==2:
		R_Number_list.read()
		for i in R_Number_list.Number_list:
			print(Al_Name.name_list[i])
			file_name1.write_file(Al_Name.name_list[i])	#写文件
			file_name1.write_file(', ')
		break

##
file_name1.cloose_file				#关文件
##
