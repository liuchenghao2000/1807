#coding=utf-8
#进程间通信
#爬虫时会使用应该
import time
from multiprocessing import Manager, Pool

def banzhuan(q):
	for i in range(4):
		time.sleep(1)
		q.put('第%d块砖'%i)
		print('放了第%d块砖'%i)

def qiqiang(q):
	while True:
		if q.empty()==False:
			for i in range(q.qsize()):
				time.sleep(1)
				print(q.get())

p = Pool()		#创建无限大的池子
q = Manager().Queue()	#进程池请用，manager方法
'''
p.apply(banzhuan,(q,))	#阻塞添加
p.apply(qiqiang,(q,))
'''
p.apply_async(banzhuan,(q,))	#非阻塞
p.apply_async(qiqiang,(q,))

p.close()
p.join()
