#判断字符串

class Panduan():
	def __init__(self,numb):
		self.numb=numb

	def panduan(self):
		try:
			if type(int(self.numb))==int:
				print('类型为数字')
		except :
			print('类型是字符串')
		finally:
			print('已完成判断')

A=Panduan(input('请输入'))
#A=Panduan('13')
A.panduan()