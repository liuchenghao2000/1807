class car():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def run(self):
        print('我在狂飙')
    def jiao(self):
        print('喇叭')



class bwm(car):
    pass


class bjd(car):
    pass


class binli(car):
    pass

class maibahe(car):
    pass


bm = car('宝马','宝蓝色')
print(bm.name)
print(bm.color)
bm.run()
bm.jiao()



bjdw = car('布加迪威龙','红色')
print(bjdw.name)
print(bjdw.color)
bjdw.run()
bjdw.jiao()


bl = car('宾利','黑色')
print(bl.name)
bl.run()
bl.jiao()


mbh = car('迈巴赫','黑色')
print(mbh.name)
print(mbh.color)
mbh.run()
mbh.jiao()

