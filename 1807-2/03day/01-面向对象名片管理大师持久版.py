class CarMan():
    def __init__(self):
        self.cards = []

    def insert(self):
        d = {}
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        d['name'] = name
        d['age'] = age
        self.cards.append(d)
        self.save()

    def find(self):
        print(self.cards)

    def change(self):
        pass

    def delete(self):
        pass

    def menu(self):
        self.open()
        while True:
            num = int(input('请选择功能1、添加2、查看'))
            if num == 1:
                self.insert()
            elif num == 2:
                self.find()

    def save(self):
        with open('data.fata','w') as f:
            f.write(str(self.cards))

    def open(self):
        f = open('data.data','r')
        self.cards = eval(f.read())
        
cm = CarMan()
cm.menu()

