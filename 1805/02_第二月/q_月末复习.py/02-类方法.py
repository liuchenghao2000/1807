#
class family():
	count=0
	def __init__(self,name): 
		self.name=name
		self.__time=50
		family.count+=1
	@classmethod#类方法 从类名或者实例调用
	def test_1(cls):
		print(family.count)
	@staticmethod#静态方法 
	def test_2():
		print(family.count)

A=family('西瓜')
B=family('桃子')
C=family('香蕉')
#静态方法
#family.test_1()
#B.test_1()
#C.test_1()

#A.test_2()
#B.get()