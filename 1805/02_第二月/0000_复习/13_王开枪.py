#王开枪
class Human():
	def __init__(self,name):
		self.name=name
		self.HP=100
		self.Gunlist=[]
	def Man_Get_gun(self):
		self.Gunlist.append(self.name)
		print('拿枪')
	def Man_Get_DJ(self,gun):
		gun.Get_danjia(self)
	def Man_Get_ZD(self,danjia,zidan):
		danjia.input_ZD(zidan)
	def Man_Fire_G(self,danjia,zidan,diren):
		danjia.ouput_ZD()
		zidan.kill_Hp(diren)
	def Tell_hp(self):
		print(self.HP)

class Guns():
	def __init__(self,name):
		self.name=name
	def Get_danjia(self,man):
		man.Gunlist.append(self.name)
class Gun_danj():
	def __init__(self,name,Number):
		self.name=name
		self.ZiDan_list=[]
		self.DJ_Number=Number
	def input_ZD(self,zidan):
		self.ZiDan_list.extend(zidan.ZD_Number)
	def ouput_ZD(self):
		self.ZiDan_list.pop()
class Gun_zidan():
	def __init__(self,name,Number,HP):
		self.name=name
		self.ZD_Number='*'*Number
		self.HP=HP
	def kill_Hp(self,diren):
		diren.HP-=self.HP

A=Human('wang')
B=Guns('木手枪')
C=Gun_danj('弹夹',3)
D=Gun_zidan('子弹',20,5)

di=Human('敌人')
A.Man_Get_gun()
A.Man_Get_DJ(B)
A.Man_Get_ZD(C,D)
while True:
	A.Man_Fire_G(C,D,di)
	if di.HP==5:
		break
di.Tell_hp()