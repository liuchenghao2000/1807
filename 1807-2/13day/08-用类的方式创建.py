from multiprocessing import Process
import time

class MyProcess(Process):
	def __init__(self):
		super().__init__()

	def run(self):
		for i in range(10):
			time.sleep(1)
			print('我爱老王')


P = MyProcess()
P1 = MyProcess()
P.start()
P1.start()
P.join(3)
print('吃喝玩乐')

	