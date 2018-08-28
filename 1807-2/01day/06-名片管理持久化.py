list = []
def a():
    while True:
        str = {}
        name = input('请输入名字:')
        age = input('请输入年龄')
        str['name'] = name
        str['age'] = age
        list.append(str)
        print(list)
        w()

def w():
    f = open('名片.txt','w')
    f.write(str(list))
    f.close()
    r()

'''
def d():
    f2 = open('名片.txt','a')
    f2.write(list)
    f2.close()
    r()
'''
def r():
    f1 = open('名片.txt','r')
    content = f1.read()
    if len(content) != 0:
        print(type(content))
        list = eval(content)
        for i in list:
            for k,v in i.items():
                print(k,v)
        print(list)
    f1.close()
a()



