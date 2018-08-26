import time
import re

#旅馆系统
class hotel():
	def __init__(self):
		self.jiage=10
		self.peopel={}
		self.InHouse=0
		self.OutHouse=0
		self.timeHouse=0
	def main(self):
		while True:
			arg=input('-选择以下功能-\n1.---入住---\n2.---离店---\n3.---统计---\n4.---退出---')
			if arg == '1':
				self.In_house()
			if arg == '2':
				self.Out_house()
			if arg == '3':
				self.count_money()
			if arg == '4':
				self.exit_system()
				break
	def In_house(self,x):	#增
		a =ManInt()
		if x.name != None:
			self.peopel[x.name]=(x.phoneTel,x.The_time)
			self.In_house+=1
	def Out_house(self,x):	#删
		a =ManInt()
		for k,v in items(self.peopel):
			if k==x:
				The_time_1=time.time()
				x.cou=The_time_1-x[1]
				print('总住宿支出%.02f元'%(cou*self.jiage))
				self.timeHouse+=x.cou
				self.peopel.pop(x.name)
				self.OutHouse+=1
			else:
				print('查无此人')
	def count_money(self):	#统计收入
		print('本日住店人数%d'%(self.InHouse))
		print('本日离店人数%d'%(self.OutHouse))
		print('本日总收入%f'%(self.timeHouse*10))

	def exit_system(self):
		print('退出系统')

#个人信息记录
class ManInt():
	def __init__(self):
		while True:
			self.name = input('请输入名字')
			self.x = input('请输入手机号')
			if (re.match('^1[3-9]\d{9}$',self.phoneTel))!=None:
				self.phoneTel=self.x
				break
			else:
				print('手机号输入错误')
EVE=hotel()

EVE.main()