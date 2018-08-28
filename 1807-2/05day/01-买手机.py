class Phone():
    def __init__(self,name,color):
        self.name = name 
        self.color = color

    def call(self):
        print('打电话')
    

class meizi(Phone):
    pass

class huawei(Phone):
    pass

mz = meizu('魅族','白色')
print(mz.name)
print(mz.color)
mz.call(()

hw = huawei('华为','黑色')
print(hw.name)
print(hw.color)
hw.call()

