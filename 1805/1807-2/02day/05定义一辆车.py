class car:
    def __init__(self,color,tupe):
        self.color = color
        self.tupe = tupe
    def yidong(self):
        print('我在狂飙')
    def music(self):
        print('听音乐')
    def jieshao(self):
        print('我的%s 我的型号是%s'%(self.color,self.tupe))
a = car('宝蓝色','布加迪威龙')
a.yidong()
a.music()
a.jieshao()

