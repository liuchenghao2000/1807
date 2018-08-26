#老王开枪
class Human():
	def __init__(self,name):
		self.name=name
		self.MyGuns=[]
		self.HP=100
	def Get_Guns(self,qiang):					#拿枪
		if len(self.MyGuns)<2:
			self.MyGuns.append(qiang.name)
			self.flag_1=0
			print('以拿枪')
		else:
			print('已持有2把\n超载')
	def in_DJia(self,Guns,danjia):				#弹夹
		if len(Guns.MyD_Jia)<3:
			Guns.Get_Djia(danjia)
			self.flag_2=0
			print('以装弹夹')
		else:
			print('已持有3把\n超载')
	def in_Zdan(self,danjia,zidan):				#子弹
		danjia.Get_Zdan(zidan)
		self.flag_3=0
		print('以装弹')
	def fire_gun(self,danjia,zidan,diren):		#开火
		if self.flag_1==0 and self.flag_2==0 and self.flag_3 ==0:
			danjia.put_Zdan(zidan,diren)
			print(diren.tell_Hp())
		else:
			print('缺少')
	def down_gun(self):
		sGun=input('你想丢掉哪个枪')
		if sGun in self.MyGuns:
			self.MyGuns.remove(sGun)
		else:
			print('无此枪')
	def tell_Hp(self):
		if self.HP>=0:
			return self.HP
		else:
			return 0
class Guns():
	def __init__(self,name):
		self.name=name
		self.MyD_Jia=[]
	def Get_Djia(self,danjia):
		self.MyD_Jia.append(danjia.name)
class DanJia():
	def __init__(self,name):
		self.name=name
		self.MyZ_dan=[]
	def Get_Zdan(self,zidan):
		self.MyZ_dan.extend((zidan.icon))
	def put_Zdan(self,zidan,ren):
		if len(self.MyZ_dan)>0:
			self.MyZ_dan.pop()
			zidan.kill_diren(ren)
		else:
			print('无弹药')
class ZiDan():
	def __init__(self,name,hp,number):
		self.name=name
		self.KillHp=hp
		self.icon='#'*number
	def kill_diren(self,ren):
		ren.HP-=self.KillHp
Supman=Human('少吃Z醒')
AirGun=Guns('空气炮')
NoAir=DanJia('真空包囊')
Air=ZiDan('空气炮',30,5)
diren=Human('王宋')

Supman.Get_Guns(AirGun)
Supman.in_DJia(AirGun,NoAir)
Supman.in_Zdan(NoAir,Air)
Supman.fire_gun(NoAir,Air,diren)
Supman.fire_gun(NoAir,Air,diren)
Supman.fire_gun(NoAir,Air,diren)
Supman.fire_gun(NoAir,Air,diren)

print(diren.tell_Hp())