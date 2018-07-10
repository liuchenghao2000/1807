#ren

class Human():
	def __init__(self,):
		self.hand='1'
		self.food='2'
		self.__sleep='10'
	def Eat(self):
		print('吃饭')
	def shuijiao(self):
		return self.__sleep
	def __fly(self):
		print('fly')
	def somedo(self):
		self.__fly()

class woman(Human):
	def Feature(self):
		print('柰子脾鼓大摆退')
class man(Human):
	def Feature(self):
		print('喉结熊猫小清掉')

human = Human()

girl =woman()
boy = man()

girl.Feature()
girl.Eat()
boy.Feature()
boy.Eat()
print(boy.shuijiao())
#print(boy.somedo())
boy.somedo()