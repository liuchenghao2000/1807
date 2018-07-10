#烤地瓜
import time
class tudou():
	#初始化
	def __init__(self):
		self.tl=[]
		self.time = 0
		self.staty ='生的'
		self.a=0
	#烹饪
	def cook(self):
		self.time+=1
		if self.time<=5:
			self.staty='生的'
		elif self.time>5 and self.time<=10:
			self.staty='半熟'
		elif self.time>10 and self.time<=15:
			self.staty='熟了'
		elif self.time>15 and self.time<=20:
			self.a+=1
			self.staty='碳状物 #滑稽脸 哈哈哈 \n黑暗指数'+str(self.a)+'星'
		elif self.time>20:
			self.staty='灰灰灰烬'
	#添调料
	def addtl(self,r):
		self.tl.append(r)
	#打印
	def print_p(self):
		print('*'*30)
		print(self.staty)
		print('佐料有：%s'%str(self.tl))
		print('-'*20)
		print(' ')

gua = tudou()
fire_time = int(input('输入烤多久时间'))
for i in range(fire_time):
	gua.cook()
	if i == 2:						#重新写的
		gua.addtl('深井盐')
	elif i == 5:
		gua.addtl('花籽油')
	elif i == 7:
		gua.addtl('玫瑰蜜')
	elif i == 10:
		gua.addtl('红砂糖')
	gua.print_p()
	time.sleep(0.8)