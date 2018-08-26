#批量重命名
import os
class Change_Files():
	def __init__(self):
		self.dir_name =input('请输入文件夹名字')
		self.files=os.listdir(self.dir_name)
	def Change_name(self):
		for file in self.files:
			#名字部分		文件 	路径		文件名部分
			od_name=self.dir_name+'/'+file
			ew_name=self.dir_name+'/'+input('输入')+file
			os.rename(od_name,ew_name)
Cf=Change_Files()
Cf.dir_name
Cf.Change_name()