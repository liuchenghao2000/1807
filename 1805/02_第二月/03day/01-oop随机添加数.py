#随机添加数
import random
class Add_number():
	def __init__(self):
		self.numberlist=[]		
	def __str__(self):
		return ' '

	def Add_ber(self,x):
		if number in self.numberlist:
			pass
		else:
			self.numberlist.append(x.n)
	def tell_number(self):
		print(self.numberlist)

class rdom_number():
	def __init__(self):
		self.n= 0
	def __str__(self):
		return str(self.n)
	def ran_number(self):
		self.n=random.randint(1,100)

A_num =Add_number()

while True:
	number = rdom_number()			#创建数
	number.ran_number()
	print(number.n)					#打印数
	A_num.Add_ber(number)			#添加数
	A_num.tell_number()				#提示
	if len(A_num.numberlist)==3:	#停止
		break
