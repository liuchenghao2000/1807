#方法集合
'''
class haha():
	@staticmethod
	def add(a,b):
	     return a+b
	@classmethod
	def A_print():
		print('哈哈哈')
		print('呵呵呵')
		print('嘿嘿嘿')

#hhhh=haha()
#add(1,2)
c=haha.add(1,2)
print(c)
haha.A_print()
bb=haha()
bb.A_print()#无法显示
def dd():
	print('dd()')

dd()

def get_some(c_obj):		#返回功能的函数
	return c_obj.arg		#返回对象行为
class Kls(object):			#类
	arg=0					#类属性
	def __init__(self):		#实例属性初始值
		Kls.arg+= 1			#每有一个加1


i_1=Kls()
i_2=Kls()
print(get_some(Kls)) 		#调用函数
'''
