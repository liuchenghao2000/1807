#输入异常
class Number_some():
	def __init__(self):
		self.a=input('输入a的值')
	def Try_exception(self):
		try:
			if type(int(self.a))==int:
				print('是纯数字字符串')
			else:
				print('是字符串')
		except (NameError,KeyboardInterrupt):
			print('输入错误类型')
		except Exception as ret:
			print(ret)
			print('不知道的错误类')
		else:
			print('瞎写')
A_num=Number_some()
A_num.a
A_num.Try_exception()
