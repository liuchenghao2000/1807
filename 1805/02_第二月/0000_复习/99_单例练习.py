#单例

class Danli():
	__instance = None
	__flag = True
	def __new__(cls,name,age):
		if cls.__instance==None:
			cls.__instance=object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name,age):
		if  self.__flag:
			self.name =name
			self.age =age
			self.__flag=False

A=Danli('老王',1)
B=Danli('老宋',20)
print(id(A))
print(id(B))
print(A.name)
print(A.age)
B.age=8
C=Danli('老赵',50)
print(B.name)
print(B.age)
print(C.name)
print(C.age)
print(id(C))
