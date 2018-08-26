class Animal():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('吃')

    def sleep(self):
        print('睡')


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Pig(Animal):
    pass


jf = Cat('加菲')
print(jf.name)
jf.eat()
jf.sleep()


wc = Dog('旺财')
print(wc.name)
wc.eat()
wc.sleep()


pq = Pig('佩琪')
print(pq.name)
pq.eat()
pq.sleep()


