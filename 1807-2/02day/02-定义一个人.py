class people:
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
    def play(self):
        print('玩')
    def introduce(self):
        print('我的年龄是%d 我的身高是%d'%(self.age,self.height))


laowang = people()
laowang.eat()
laowang.sleep()
laowang.play()
laowang.age = 18
laowang.height = 165
laowang.introduce()
'''
print(laowang.age)
print(laowang.height)
'''

laoliu = people()
laoliu.eat()
laoliu.sleep()
laoliu.play()
laoliu.age = 19
laoliu.height = 173
laoliu.introduce()
'''
print(laoliu.age)
print(laoliu.height)
'''

