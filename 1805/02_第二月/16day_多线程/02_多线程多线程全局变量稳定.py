from threading import Thread, Lock
import time
#准确值方法	flag while True:
#			lock
#互斥锁
num=0
def work1():
	global num
	for i in range(1000000):
		mutex.acquire(True)	#阻塞上锁
		num += 1
		mutex.release()		#释放锁
	print('线程一：%d'%num)
def work2():
	global num
	for i in range(1000000):
		mutex.acquire(True)	#阻塞上锁
		num += 1
		mutex.release()		#释放锁
	print('线程二：%d'%num)

t1 = Thread(target=work1)
t2 = Thread(target=work2)
mutex = Lock()

t1.start()
t2.start()
