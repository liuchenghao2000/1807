class A():
    def __init__(self):
        self.name = 10
        self.age = 20

    def show(self):
        print('哇哈哈哈 A')



class B():
    def show1(self):
        print('额呵呵呵')




class C(A,B):
    pass



c = C()
print(c.name)
print(c.age)
c.show()
c.show1()
print(c.age)

