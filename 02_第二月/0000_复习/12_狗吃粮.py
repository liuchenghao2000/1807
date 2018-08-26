#吃粮
class Animal():
	def __init__(self,name,size):
		self.name=name
		self.size=size
		self.list=[]
	def import_food(self,x):
		self.size+=x.size
		self.list.append(x.name)
		print('能量为%d'%self.size)
	def degist_food(self,x):
		self.size-=x
		print('消化了%d份能量'%x)
	def tell_power(self):
		if self.size>0 and self.size<=30:
			print('饥饿')
		elif self.size>30 and self.size<=50:
			print('温饱')
		elif self.size>50 and self.size<=80:
			print('很饱')
		elif self.size>80 and self.size<100:
			print('撑了')
class Foods():
	def __init__(self,name,size):
		self.name=name
		self.size=size
import time
Dog=Animal('狗',10)
rice=Foods('米',50)
i=0
while True:
	if i %8==0:
		Dog.import_food(rice)
	Dog.degist_food(5)
	if i%10==0:
		Dog.tell_power()
	if Dog.size>100:
		print('撑死')
		break
	time.sleep(0.4)
	i += 1