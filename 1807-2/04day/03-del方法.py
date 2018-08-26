class Dog():
    def __init__(self):
        self.name = '二哈'
        print('init')


    def __str__(self):
        return '我为str方法'



    def __del__(self):
        print('我del')#当一个对象没有任何引用指向它的时候会执行



dog = Dog()
print(dog)
dog1 = dog
del dog
del dog1
print('0')

