#单例模式
class Testsome(object):
	__instance=None
	__flas = False
	def __new__(cls,*a,**v):#方法
		if not cls.__instance:#
			cls.__instance=object.__new__(cls)
		return cls.__instance
		
	def __init__(self,name):
		if not Testsome.__flas:
			print('初始化播放器')
			self.name=name
			Testsome.__flas=True
C=Testsome('虫')
			
A=Testsome('狗')
B=Testsome('猫')
print(A)
print(B)
print(C)
print(A.name)
