#装饰器		#game
def game(x,y):
	def game1(y):
		print('欢迎进入亡者峡谷')
		if y ==1:
			print('孙悟空')
		elif y ==2:
			print('崔斯特')
	def game2(y):
		print('欢迎进入吃鸡战场')
		if y ==1:
			print('平顶锅')
		elif y ==2:
			print('屁股')
	def account(fun):
		fun()
	return game
@game(1，2)
def information():
	name = input('请输入名字')
	print(name)