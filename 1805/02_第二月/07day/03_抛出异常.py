#假如老王  抛出异常
class somefile():
	def __init__(self):
		self.name=input('输入名字')

	def error_get(self):
		try:
			if self.name=='laowang':
				raise ShowError(laowang)
		except:
			print('ShowError:输入的名字是:%s 名字应不是:%s'%(self.name,self.name))
		else:
			print('无异常')


cc=somefile()
cc.name
cc.error_get()

