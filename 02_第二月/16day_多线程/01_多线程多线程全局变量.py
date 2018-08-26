from threading import  *
import time


num=0
def work1():
	global num
	for i in range(1000000):
		num += 1
	print('线程一：%d'%num)
def work2():
	global num
	for i in range(1000000):
		num += 1
	print('线程二：%d'%num)

t1 = Thread(target=work1)
t2 = Thread(target=work2)

t1.start()
t2.start()
1