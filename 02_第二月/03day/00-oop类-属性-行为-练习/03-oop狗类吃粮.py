#狗吃粮
import time
import random
class Dog():
	def __init__(self,name,color,place):
		self.name = name
		self.color = color
		self.place = place
		self.weilist  =[]
		self.savelist =[]
		self.time=0
	def __str__(self):
		return '我是'+self.name+'\n颜色是'+self.color+'\n地点在'+self.place

	def eat(self,ricedog):
		if len(self.weilist)<=25:
			self.weilist.extend(ricedog.power)
		else:
			self.savelist.extend(ricedog.power)
	def tell_stat(self):
		weilist=self.weilist
		if len(self.weilist)>0 and len(self.weilist)<=10:
			return '饥饿'
		elif len(self.weilist)>10 and len(self.weilist)<=20:
			return '温饱'
		elif len(self.weilist)>20 and len(self.weilist)<=25:
			return '非常饱'
		elif len(self.weilist)>25:
			return '吃不下了 保存起来'
	def time_wei(self):
		self.time+=1
		if self.time%3==0:
			self.weilist.pop()
			print(self.weilist)
			print('消化了一个能量\t')
			print(len(self.weilist))
			time.sleep(0.8)

class Food():
	def __init__(self,brank,place,power):
		self.brank=brank
		self.place=place
		self.power='@'*power
	def __str__(self):
		return '品牌是'+self.brank+'\n产地在'+self.place

dsendog = Dog('单身狗','绿色','地球')
ricedog = Food('老王牌','隔壁',random.randint(1,3))			#定类
for i in range(10):
	dsendog.eat(ricedog)#ricedog.Food_power())		#吃
	dsendog.time_wei()						#消化
	print(dsendog.tell_stat())						#告诉
	time.sleep(0.5)
	#print(dsendog)
	#print(ricedog)

