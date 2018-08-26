class Dog():
    print('哈哈哈哈哈')
    count = 100
    __count1 = 200
    def __init__(self,name):
        self.name = name
        sefl.__age = age

    def getAge(self):
        return self.__age

    @classmethod
    def getCount(cls):
        return cls.count

    @classmethod
    def getCount1(cls):
        return cls.__count1

qq = Dog('圈圈')
print(qq.name)
print(qq.age)
Dog.getCount()
print(Dog.getCount1())
