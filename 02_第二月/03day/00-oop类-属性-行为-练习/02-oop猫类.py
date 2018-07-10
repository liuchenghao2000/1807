#cat
class cat():
	def __init__(self,size,color):
		self.species= 'china'
		self.size =size
		self.color = color
		self.rand_er=random.randint(1,3)
	def __str__(self):
		return '这个猫'+self.size+'\n颜色是'+self.color+'\n品种是'+self.species

	def name(self):
		print(a)
		return 'hahaha'

	def food(self):
		b = self.rand_er
		if b ==1:
			print('猫粮')
		elif b==2:
			print('鱼')
		elif b==3:
			print('曲子')
	#def ran_numb(self):

import random

a = '崔睿'
#b = random.randint(1,3)

cat_china = cat('非常大','black')
print('1',cat_china)			#调用__str__返回
print('2',cat_china.name)		#地址返回  打印返回
print('3',cat_china.name())		#调用xx返回
print('4 ',end='')
cat_china.name()				#调用打印
print('5')
print('6',cat_china.food)
print('7',cat_china.food())
print('8',)
print("9",end='')
cat_china.food()