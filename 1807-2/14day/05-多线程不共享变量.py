from threading import Thread
import time

def work(i):
    num = 0
    time.sleep(i)
    num+=1
    print(num)

def work1(i):
    num = 0
    time.sleep(i)
    num+=2
    print(num)


w = Thread(target=work,args=(3,))
w1 = Thread(target=work1,args=(5,))
w.start()
w1.start()
