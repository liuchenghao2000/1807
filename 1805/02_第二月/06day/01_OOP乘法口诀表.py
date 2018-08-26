#乘法口诀
class Number():
	def __init__(self):
		self.aa='123456789'
		self.bb='123456789'
class Multiply(Number):
	def Mul_AB(self):
		for  i in self.aa:
			for u in self.bb:#[::-1]:
				if u<=i:
					print('%s*%s=%d'%(u,i,int(i)*int(u)),end='\t')
			print('')
some=Multiply()
some.Mul_AB()