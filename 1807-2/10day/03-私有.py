class Dog():
    def __init__(self,name):
        self.name = name
        self.__age = 70

    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

dog = Dog('旺财')
print(dog.name)
print(dog.getName())
print(dog.getAge())

