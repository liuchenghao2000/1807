#进程测试
import os
import time


gg = os.fork()
if gg==0:
	time.sleep(3)
	print('我是子%s,我父%s'%(os.getpid(),os.getppid())) 
else:
	time.sleep(5)
	print('我是父%s,我爹%s'%(os.getpid(),os.getppid())) 
