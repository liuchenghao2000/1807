list = []

def menu():
    print("欢迎来到本旅馆")
    while True:
        print("1、入住")
        print("2、离店")
        print("3、统计")
        print("4、退出")
        break 
    a()

def a(): 
    while True:
        num = int(input("请选择功能:"))
        if num == 1:
            add()
        elif num == 2:
            lidian()
        elif num == 3:
            tongji()
        elif num == 4:
            exit()
            break


def add():
    str = {}
    while True:    
        name = input("请输入姓名:")
        id = input("请输入身份证号码:")
        if len(id) == 18:
            print("入住成功")
        else:
            print("请重新输入")
        list.append(str)
        print("姓名:%s\n身份证号码:%s"%(["name"],["id"]))
        break

def lidian():
    flag = False
    name = input("请输入离店人姓名:")
    for i in list:
        if str["name"] == name:
            list.remove(name)
            print("删除成功")
    if not flag:
        print("查无此人")

def tongji():
    pass


def exit():
    print("欢迎使用")
menu()



















