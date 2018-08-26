class Dog():
    print('哈啊哈哈哈')
    def __init__(self,name):
        self.name = name
        self.__age = 10


    def getAge(self):
        return self.__age


qq = Dog('圈圈')
print(qq.name)
print(qq.getAge())
