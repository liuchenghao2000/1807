#多进程
import time
from multiprocessing import Process


p = Process(target=(args='hehe',))
print('子进程将开启')
time.sleep(2)
p.start()
p.join()
print('子进程已结束')

