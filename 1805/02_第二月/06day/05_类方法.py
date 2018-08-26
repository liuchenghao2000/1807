'''
#工具类
class Tool():
	count = 0
	def __init__(self,name):
		self.Name = name
	@classmethod
	def GetCount(cls):
		cls.count+=1
		return cls.count
Fuzi = Tool('fuzi')
Caidao = Tool('caidao')
Anban = Tool('anban')
Banshou = Tool('banshou')
Fuzi.Name
print(Tool.GetCount())#类调用#可能干扰
print(Fuzi.GetCount())#对象调用
'''
#工具类
class Tool():
	count = 0
	cc = 0
	def __init__(self,name):
		self.Name = name
		Tool.cc+=1
	@classmethod
	def GetCount(cls):
		cls.count+=1
		return cls.count
	def someToo():
		return '帅'
Fuzi = Tool('fuzi')
Caidao = Tool('caidao')
Anban = Tool('anban')
Banshou = Tool('banshou')
Fuzi.Name
print(Tool.GetCount())#类调用#可能干扰
print(Fuzi.GetCount())#对象调用
print(Tool.cc)
Banshou.someToo()