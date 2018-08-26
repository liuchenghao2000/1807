import time

def writeLog(msg):
    with open('log.txt','a') as f:
        f.writhe(msg)

def w1(fun):
    def inner(*args,**kwargs):
        msg = str(fun) + str(time.ctime()) +'\n'
        writheLog(msg)
        fun(*args,**kwargs)
    return inner

class Hotel():
    def __init__(self,name):
        self.name = name
        self.list = []
        self.money = 0
    @w1
    def inHome(self,person):
        person.time = int(time.time())
        person.islive = True
        self.list.append(person)
    @w1
    def outHome(self,name):
        for person in self.list:
            if person.name == name:
                person.islive = False
                endtime = int(time.time())
                diff_money = (endtime - person.time)*10
                print('花了%.02f'%diff_money)
                self.money += diff_money
                break
    @w1
    def tongji(self):
        count = 0
        for person in self.list:
            if not person.islive:
                count += 1
            print('今天总入住%d人；收入%.02f'%(len(self.list),count,self.money))

class Person():
    def __init__(self,name):
        self.name = name
    def setCard(self,card):
        if len(card) == 3:
            self.card = card


rj = Hotel('如家')
while True:
    num = int(input('请选择功能 1、住 2、离 3、统 4、退'))
    if num == 1:
        name = input('请输入名字')
        card = input('请输入身份证')
        lz = Person(name)
        lz.setCard(card)
        rj.inHome(lz)
    elif num == 2:
        name = input('请输入名字')
        rj.outHOme(name)
    elif num == 3:
        rj.tongji()
    elif num == 4:
        exit()


