#老王开抢
class Human():					#人类
	def __init__(self,name1):
		self.name=name1
		self.HP=100
		self.Hand_List=[]		#最大持有为3
	def Get_Guns(self,guns):
		self.Hand_List.append(guns.name)
	def Tell_Guns(self):
		print('持有的枪有')
		print(self.Hand_List)
	def Tell_HP(self):
		if self.HP>0:
			print(str(self.HP))
		elif self.HP==0:
			print('目标已死亡')
	def Fire_Guns(self):
		print('开枪')

class Guns():
	def __init__(self,name2):
		self.name=name2
		self.D_Jialist=[]#最大持有为2

	def Import_D_Jia(self,d_jia):
		if len(self.D_Jialist)<2:
			self.D_Jialist.append(d_jia)
		else:
			pass
	def Tellme_D_jia(self):
		print('弹夹有%d个'%len(self.D_Jialist))

class D_Jia():
	def __init__(self,name3):
		self.name=name3
		self.D_Yaolist=[]#最大持有为40

	def Import_D_Yao(self,d_yao):
		if len(d_jia.D_Yaolist)<40:
			d_jia.D_Yaolist.append(d_jia)
		else:
			pass
	def Outport_D_Yao(self,d_yao):
		if len(d_jia.D_Yaolist)>0:
			d_jia.D_Yaolist.pop()
			flag=1
			global flag
		else:
			print('无弹药')
	def Tellme_D_yao(self):
		print('有%d弹药'%len(d_jia.D_Yaolist))

class D_Yao():
	def __init__(self,name4,shanghai):
		self.name=name4
		self.shanghai=shanghai
	def kill(self,diren):
		diren.HP-=self.shanghai
import time
#
human= Human('老王')

guns = Guns('时空空气炮')
d_jia= D_Jia('哆啦A梦口袋')
d_yao= D_Yao('压缩空气',20)

diren= Human('老宋')

qiang=Guns('超能量机械湮灭方程式')
j_qiang=D_Jia('冥王星')
d_qiang=D_Yao('质子',50)


human.Get_Guns(guns)		#获得枪
for u in range(5):
	d_jia.Import_D_Yao(d_yao)	#装弹
	d_jia.Tellme_D_yao()		#提示弹药数量
	guns.Import_D_Jia(d_jia)	#装弹夹
	if u%4==0:
		guns.Tellme_D_jia()			#提示弹夹数量
for i in range(5):			#x发子弹
	flag =0
	human.Fire_Guns()		#开枪
	d_jia.Outport_D_Yao(d_yao)	#弹出子弹判断是否有子弹
	if  flag==1:
		d_yao.kill(diren)
	diren.Tell_HP()				#告诉血量
	human.Tell_Guns()			#我的枪
	print(' ')
	time.sleep(3)
'''
human.Get_Guns(qiang)
for u in range(3):
	j_qiang.Import_D_Yao(d_qiang)	#装弹
	j_qiang.Tellme_D_yao()		#提示弹药数量
	qiang.Import_D_Jia(j_qiang)	#装弹夹
	if u%4==0:
		qiang.Tellme_D_jia()			#提示弹夹数量
for i in range(5):			#x发子弹
	flag =0
	human.Fire_Guns()		#开枪
	j_qiang.Outport_D_Yao(d_qiang)	#弹出子弹判断是否有子弹
	if  flag==1:
		d_yao.kill(diren)
	diren.Tell_HP()				#告诉血量
	human.Tell_Guns()			#我的枪
	print(' ')
	time.sleep(3)
'''