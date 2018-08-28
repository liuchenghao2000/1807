import os

pid = os.fork()
if pid == 0:
	print('呵呵呵')
else:
	print('哈哈哈')