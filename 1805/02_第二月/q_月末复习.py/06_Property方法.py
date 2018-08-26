class GetSetTest():
	def __init__(self,age):
		self.__age=age

#	def getAge(self):
#		print(self.__age)
#	def setAge(self,age):		#方法一
#		if age>=0:
#			self.__age=age
#		else:
#			print('年龄不能为负')
#	age=property(getAge,setAge)	#方法二
	
	@property
	def age(self):
		return self.__age
	@age.setter					#方法三
	def age(self,age):
		if age>=0:
			self.__age=age
		else:
			print('年龄不能为负')
A=GetSetTest(18)
#A.setAge(12)		#1改
#A.age=47			#2改
A.age=8				#3改
print(A.age)
#A.getAge()			#1,2获取