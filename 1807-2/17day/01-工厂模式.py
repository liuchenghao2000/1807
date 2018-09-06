class Car():
	def __init__(self,color):
		self.color = color

	def run(self):
		print('--run')


class Bmw(Car):
	def __init__(self,color):
		self.count = 6
		super().__init__()

	def run(self):
		print('bmw--run')


class BenChi(Car):
	def run(self):
		print('BenChi--run')


class BieKe(Car):
	def run(self):
		print('BieKe--run')


class Factory():
	def create(self):
		pass


class BmwFactory(Factory):
	def create(self):
		return Bmw()

class BenChiFactory(Factory):
	def create(self):
		return BenChi()

class BieKeFactory(Factory):
	def create(self):
		return BieKe()

class CarFactory(Factory):
	def create(self,type):
		if type == 1:
			return Bmw()
		elif type == 2:
			return BenChi()
		elif type == 3:
			return BieKe()

bmw = BmwFactory().create('红色')
benchi = BenChiFactory().create('黑色')
bieke = BieKeFactory().create('白色')

















