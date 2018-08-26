#装家具
class Home():
	def __init__(self,place,size):
		self.place=place
		self.size=size
		self.surplus=size
		self.Homelist=[]
	def __str__(self):
		return '房子地址在:'+self.place+'\n面积大小有:'+str(self.size)+'㎡'+'\n剩余面积有'+str(self.surplus)+'㎡'

	def input_jiaju(self,Jiaju):
		if self.surplus>=chuang.J_size:
			self.Homelist.append(Jiaju)
			self.surplus-=chuang.J_size
			print('已添加')
		else:
			print('无位置')

class Jiaju():
	def __init__(self,blank,J_size):
		self.blank=blank
		self.J_size=J_size
	def __str__(self):
		return '床的品牌是：'+self.blank+'\n床的大小是：'+str(self.J_size)+'㎡'

Myhouse =Home('迈阿密',100)
chuang = Jiaju('林肯居家',20)

for i in range(6):
	print(Myhouse)
	print(chuang)
	Myhouse.input_jiaju(chuang)