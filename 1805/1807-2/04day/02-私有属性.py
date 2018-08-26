class Dog():
    def __init__(self):
        self.name = '' 
        self.__age = 0

    def sleep(self):
        print('11')


    def setAge(self,age):
        if age > 15 or age < 1:
            print('输入错误')
        else:
            self.__age = age

    def getAge(self):
        return self.__age



eh = Dog()
eh.setAge(13)
print(eh.getAge())

