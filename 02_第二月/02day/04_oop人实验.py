'''
class humen():
	def sex(self):
		print('男性\n女性')
	def age(self):
		print('童年\n少年\n中年\n老年')
	def color(self):
		print('白色\n黄色\n黑色')
	def introduce(self):
		print(self.color())

people = humen
people.color='棕色'
people.sex()
people.introduce()
'''
class humen():
	def __init__(self,newcolor,newage,newsex):
		self.color = newcolor
		self.age = newage
		self.sex = newsex

	def  __str__(self):
		msg = '您好，基本信息以加载完成:\n性别:'+self.sex+',\n肤色:'+self.color+'\n年龄'+str(self.age)
		return msg

	def move(self):
		print('在香港旅行，准备去澳门 #滑稽脸')

cr = humen('yellow',21,'男')

ishumen = isinstance(cr,humen)

print('MY'.center(20,'*'))
print('性别为:%s'%cr.sex)
print('肤色为：%s'%cr.color)
print('年龄为：%s'%cr.age)
print()
print('内存地址：',id(cr))
print(cr)