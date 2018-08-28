from multiprocessing import Pool
import time


def show(num):
	for i in range(10):
		time.sleep(1)
		print('哈哈哈哈%d'%num)

p =Pool()
for i in range(10):
	#p.apply_async(show,(i,))
	p.apply(show,(i,))


	print('添加成功')

p.close()
p.join()
print('呵呵呵')