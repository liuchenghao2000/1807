#记录实例创建次数
class family():
	count=0
	def __init__(self,name='大哥'):
		self.name=name
		family.count+=1

class parent(family):
	pass

A=parent()
B=parent('小弟')
C=parent('马崽')
print(family.count)


print(A.name)
print(B.name)
print(C.name)
