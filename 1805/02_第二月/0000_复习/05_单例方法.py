#单例
class Test1_some(object):	#保证只有1个对象
	__instance=None
	__flag=True
	def __new__(cls,age,name):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init__(self,age,name):
		if self.__flag==True:
			self.name=name
			self.age=age
			self.__flag=False

A=Test1_some(1,'cui')
B=Test1_some(2,'ren')
C=Test1_some(3,'chang')

print(id(A))
print(id(B))
print(id(C))
A.age=18
print(A.age)
print(B.age)
print(C.age)