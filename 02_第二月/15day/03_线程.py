'''
#单线程练习
import time


def saySorry():
	print('亲爱的，我错了，我能吃饭了么')
	time.sleep(2)

if __name__=='__main__':
	for i in range(5):
		saySorry()
'''
'''
#多线程练习
import threading
import time


def saySorry():
	print('亲爱的，我错了，我想吃饭了')
	time.sleep(2)

if __name__=='__main__':
	for i in range(5):
		t = threading.Thread(target=saySorry)#关键句
		t.start()
'''
import threading
from time import sleep,ctime

def sing():
	for i in range(3):
		print('正在唱歌...%d'%i)
		sleep(1)
def dance():
	for i in range(3):
		print('正在唱歌...%d'%i)
		sleep(1)

if __name__=='__main__':
	print('---开始---:%s'%ctime())
	t1 = threading.Thread(target=sing)
	t2 = threading.Thread(target=dance)

	t1.start()
	t2.start()
	sleep(5)
	print('---结束---:%s'%ctime())