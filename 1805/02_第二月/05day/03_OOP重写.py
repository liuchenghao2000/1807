#爸爸赚钱
class Family():
	def Make_money(self):
		print('做生意')
class Parent(Family):
	def Make_money(self):
		print('做生产')
class Myself(Parent):
	def Make_money(self):
		print('搬砖')
class Myson(Myself):
	def Make_money(self):
		print('敲码')


cui=Myself()
cui.Make_money()
son=Myson()
son.Make_money()