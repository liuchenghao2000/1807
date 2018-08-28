import os
import time
#全局变量不共享
num = 0
pid = os.fork()
if pid == 0:
	print('子进程')
	time.sleep(3)
	if num > 1:
		print('我是老王')

else:
	print('父进程')
	num+=1