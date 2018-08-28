class Dog():
    def __init__(self):
        self.__age = 100

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age
        print('数据是'+str(self.__age))
    age = property(getAge,setAge)

dog = Dog()
#dog.setAge(150)
#print(dog.getAge())


dog.age = 900
dog.age
print(dog.getAge())

