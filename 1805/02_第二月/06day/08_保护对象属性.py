#保护对象属性方法
class A_test():
	def __init__(self,age):
		self.__secret='总是迟到'
		self.__secret_age= age
	def	protectsome(self,name,age):
		if len(name)<=4 and len(name)>=0 and age>=18:
			self.__secret=name
			self.__secret_age=age
		else:
			return '输入错了'
	def tell_me_secret(self):		
		return self.__secret,self.__secret_age#只能返回一个值
a=A_test(11)
a.protectsome('崔',19)
c=a.tell_me_secret()
print(c)
