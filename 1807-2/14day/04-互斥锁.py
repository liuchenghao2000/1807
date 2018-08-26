from threading import Thread,Lock
import time

num = 0 
def work1():
    global num
    m.acquire(True)#加锁 阻塞加锁
    for i in range(100000):
        num += 1
    m.release()
            #time.sleep(5)
    #print('thread - 1')
    print(num)
    print('thread - 1')

def work2():
    global num
    m.acquire(True)
    for i in range(100000):
        num += 1
    m.release()
                #time.sleep(8)
    #print('thread - 2')
    print(num)
    print('thread - 2')

m = Lock()
w1 = Thread(target=work1)
w1.start()
w2 = Thread(target=work2)
w2.start()
#w1.join()
#w2.join()

