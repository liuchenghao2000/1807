#单例

class Cat():
	__i = None
	__n = True
	def __new__(cls):
		if cls.__i==None:
			cls.__i= object.__new__(cls)
			return cls.__i
		else:
			return cls.__i

a=Cat()
print(a)
b=Cat()
print(b)

