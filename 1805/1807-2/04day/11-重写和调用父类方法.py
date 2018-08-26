class Dog():
    def __init__(self,name):
        self.name = name
        print('父类')

    def wark(self):
        print('汪汪汪')


class hsq(Dog):
    def __init__(self,name):
        self.name = name
        print('子类的')


class xtq(Dog):
    def wark(self):
        print('吼吼吼')
        super().wark()





hsq1 = hsq('狗蛋')
print(hsq1.name)
hsq1.wark()



xtq1 = xtq('四眼')
print(xtq1.name)
xtq1.wark()
        

