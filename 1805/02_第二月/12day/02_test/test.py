print('1')#最初
#-------------------
class test(object):
	def __init__(self,name,age):
		self.name=name
		self.__age=age
	def getAge(self):
		return self.__age
	def setAge(self,age):
		if isinstance(age,int):
			self.__age=age
		else:
			print('error:不是整形数字')
a=test('崔睿',21)
a.setAge(11)
print(a.getAge())
#-------------------
print('2')
#-------------------
class test_1(object):
	def __init__(self,name,value):
		self.name=name
		self.__age=value
	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self,value):
		if isinstance(value,int):
			self.__age=value
		else:
			print('error:不是整形数字')
m =test_1('崔睿',12)
m.age=200
print(m.age)
#----------------------------
print('3')
#-------------------
class test_2(object):
	def __init__(self,name,value):
		self.name=name
		self.__age=value

	def getAge(self): 
		return self.__age
	def setAge(self,value):
		if isinstance(value,int):
			self.__age=value
		else:
			print('error:不是整数型整数')
	age = property(getAge,setAge)

ge = test_2('崔',0)
ge.age=520
print(ge.age)
