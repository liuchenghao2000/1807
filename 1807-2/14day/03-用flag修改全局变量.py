from threading import Thread
import time

num = 1
flag = 1
def work1():
    global num,flag
    if flag == 1:
        for i in range(100000):
            num += 1
            #time.sleep(5)
        print('thread - 1')
        print(num)
        flag = 2

def work2():
    global num
    while True:
        if flag == 2:
            for i in range(100000):
                num += 1
                #time.sleep(8)
            print('thread - 2')
            print(num)
            break

w1 = Thread(target=work1)
w1.start()
w2 = Thread(target=work2)
w2.start()
#w1.join()
#w2.join()

