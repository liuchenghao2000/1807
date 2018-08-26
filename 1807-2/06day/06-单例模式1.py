class Son():
    __instance = None
    __flag = False
    def __init__(self,name):
        if Son.__flag == False:
            self.name = name
            son.__flag = True

    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance == super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

xifu = Son('小红')
print(id(xifu))
