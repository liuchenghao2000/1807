import os

rpid = os.fork()
if rpid<0:
	print('fork调用失败')
elif: rpid ==0:
	print('我是子进程(%s),我的父进程是(%s)'%(os.getpid(),os.getppid()))
	x+=1
else:
	print('我是父进程(%s),我的子进程是(%s)'%(os.getpid(),os.rpid()))

print('子父进程都可以执行代码')