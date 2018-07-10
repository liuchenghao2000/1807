#烤地瓜
import time
class fire_gua():
	#初始化
	def __init__(self):
		self.status = '生的'		#状态
		self.time = 0			#时间
		self.list = []			#佐料
		self.a=1
	#烧烤
	def fire(self):
		self.time+=1			#以前做错了
		if self.time<=6:
			self.status='生的'
		elif self.time>6 and self.time<=10:
			self.status='没熟再等一会儿'
		elif self.time>10 and self.time<=15:
			self.status='熟了'
		elif self.time>15:
			self.status='真～！黑暗料理--之--碳味地瓜'+str(self.a)+'星'
			self.a+=1
	#显示
	def tell_p(self):
		print(self.status)
		print('佐料有%s'%str(self.list))
	#加料
	def condiments(self,s):
		self.list.append(s)

cc = fire_gua()
for i in range(20):
	cc.fire()
	if i ==2:
		cc.condiments('盐')
	elif i==6:
		cc.condiments('油')
	elif i==9:
		cc.condiments('蜂蜜')
	elif i==12:
		cc.condiments('糖')
	cc.tell_p()
	time.sleep(0.5)
