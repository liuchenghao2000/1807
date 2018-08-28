list = []
def showError(msg):#显示错误
    print('输入错误,请重新输入'+msg)

def add():
    stu = {}
    while True:
        name = input('请输入学生姓名:')
        if len(name) >= 2 and len(name) <= 4:
            stu['name'] = name
            break
        else:
            print('学生姓名必须大于2小于4')
    while True:    
        age = input('请输入学生年龄:')
        if age.isdigit():
            age = int(age)
        else:
            print('输入有误')
            continue
        if age > 1 and age < 130:
            stu['age'] = age
            break
        else:
            print('学生年龄必须大于1小于130') 
    list.append(stu)
    print('添加成功')





def find():
    name = input('请输入查找姓名:')
    for stu in list:
        if stu['name'] == name:
            print('学生姓名:%s\n学生年龄:%d'%stu['name'],stu['age'])   
            break




def change():
    name = input('请输入查找姓名:')
    for stu in list:
        if stu['name'] == name:
            print('1.修改名字')    
            print('2.修改年龄')
            num = int(input('请选择功能:'))
            if num == 1: 
                name = print('请输入新的姓名:')
                stu['name'] = name
            elif num == 2:
                age = print('请输入新的年龄:')
                stu['age'] = age
            break





def delete():
    name = input('请输入要删除姓名:')
    for stu in list:
        if stu['name'] == name:
            list.remove(stu)
            print('删除成功')
            break


def print_menu():
    print('欢迎来到学生管理系统'.center(30,' '))
    while True:
        print('1.添加学生信息')
        print('2.查找学生信息')
        print('3.修改学生信息')
        print('4.删除学生信息')
        print('5.打印学生信息')
        print('6.退出学生系统')
        input_info()#调用选择功能函数



def input_info():
    num = input('请选择功能')
    if isNum(num):
        num = int(num)
    else:
        print('输入有误')
    if num == 1:
        add()
    elif num == 2:
        find()
    elif num == 3:
        change()
    elif num == 4:
        delete()
    elif num == 5:
        print_list()
    elif num == 6:
        exit()

print_menu()


