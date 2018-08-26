class my():
	def __init__(self,new_name,new_place):
		self.name = new_name
		self.place = new_place
'''
	def __str__(self):
		msg = '名字是:'+self.name+'地址是:'+self.place
		return msg
'''
cr = my('崔睿','洛阳')

print(cr.name)
print(cr.place)
print('')
print(cr)
