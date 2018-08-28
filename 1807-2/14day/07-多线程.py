from threading import Thread
import time

def work():
	for i in range(10):
		print('老王啊啊哈哈哈哈')
		time.sleep(1)

t = Thread(target=work)
t1 = Thread(target=work)
t.start()
t1.start()