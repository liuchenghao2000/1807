#装修房子
class house():
	def __init__(self,place,h_size):
		self.place=place
		self.h_size=h_size
		self.s_size=h_size
		self.homelist=[]
	def __str__(self):
		return '地点是'+self.place+'   大小有'+str(self.h_size)+'㎡'

	def add_f(self,bloor):
		if Gu_gong.s_size>=bloor.f_size:
			Gu_gong.homelist.append(bloor)
			self.s_size-=bloor.f_size
		else:
			pass
	def tell_s_size(self):
		if self.s_size>=bloor.f_size:
			print('可以添加')
			print('剩余面积是%s'%self.s_size)
		else:
			print('面积不够无法添加')

class furniture():
	def __init__(self,name,color,f_size):
		self.name=name
		self.color=color
		self.f_size=f_size
	def __str__(self):
		return '家具名字是'+self.name+'颜色是'+self.color+'\n尺寸是'+str(self.f_size)

Gu_gong=house('长安街',400)
bloor=furniture('地板','木色',40)

for i in range(10):
	print(Gu_gong)
	print(bloor)
	Gu_gong.tell_s_size()
	Gu_gong.add_f(bloor)

	print('-'*20)
