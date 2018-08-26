#魔法方法
class Test_some():
	def __init__(self):		#初始化值
		self.name='老王'

	def __str__(self):		#必须有返回值
		print('老王是你爹')
		return 'haha'
	def __del__(self):		#删除对象时调用
		print('已删除',self.name)
	#def __new__(cls):
	#	return object.__new__(cls)
# 	def __init__(self):
#       self.name='老王'

AA=Test_some()
print(id(AA))
print(AA)
print(AA)
del AA
