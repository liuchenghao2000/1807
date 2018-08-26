#房子
class House():
	def __init__(self):
		self.Hsize=400
		self.surplus=400
		self.homelist=[]
		self.flag=0
	def import_home(self,x):
		if self.surplus>=50:
			self.surplus-=x.Jhize
			self.homelist.append(x.name)
			print(self.homelist)
			print('剩余面积是%d'%self.surplus)
		else:
			print('面积不够')
			self.flag =1
#家具
class jiaju():
	def __init__(self,size,name):
		self.Jhize=size
		self.name=name

laowang=House()
bad=jiaju(50,'床')
while True:
	laowang.import_home(bad)
	if laowang.flag==1:
		break
