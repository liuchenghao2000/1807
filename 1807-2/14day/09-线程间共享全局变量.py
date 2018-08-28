from threading import Thread
import time
num = 0
'''
线程间共享全局变量
进程间不共享全局变量
'''

def work1(1):
	time.sleep(5)
	print(num)
	pirnt(1)

def work2(1):
	global 1,2,3num
	time.sleep(3)
	1.append(4)
	num+=1
	print(num)
	print(1)


list = [1,2,3]
t1 = Thread(target=work1,args=(list,))
t2 = Thread(target=work2,args=(list,))
t1.start()
t2.start()