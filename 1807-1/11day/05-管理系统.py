s = []
while True:
    print('欢迎来到学生管理系统')
    print('1:添加学生信息')
    print('2:删除学生信息')
    print('3:查找学生信息')
    print('4:修改学生信息')
    print('5:欢迎下次使用')
    a = {}
    num = int(input('请选择功能'))
    if num == 1:
        print('添加')
        name = input('请输入姓名:')
        a['name'] = name
        age = int(input('请输入年龄:'))
        a['age'] = age
        sex = input('请输入性别:')
        a['sex'] = sex
        phone = int(input('请输入电话号码:'))
        a['phone'] = phone
        print(a)
        s.append(a)
        print(s)
    #elif num == 2:
        
    elif num == 3:
        name = input('请输入学生姓名:')
        for a in s:
            if a['name'] == name:
                print('学生姓名:%s\n学生年龄:%d\n学生手机号:%d\n学生性别:%s'%(a['name'],a['age'],a['phone'],a['sex']))
                print('1:请修改姓名')
                print('2:请修改年龄')
                print('3:请修改手机号')
                print('4:请修改性别')
                num = input('请选择功能')
                if num == 1:
                    name = print('请输入新的名字')
                    a['name'] = name
                elif num == 2:
                    age = int(input('请输入新的年龄')) 
                    a['age'] = age
                elif num == 3:
                    phone == int(input('请输入新的手机号'))
                    a['phone'] = phone
                elif num == 4:
                    sex = input('请输入新的性别')
                    a['sex'] = sex
                print('修改成功')
                break
