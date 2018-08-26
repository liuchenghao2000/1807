account = 'lch'
password = 123456
i = 0
while i < 3:
    a = input('请输入账号:')
    p = int(input('请输入密码:'))
    if a == account and p == password:
        print('登陆成功')
        number = int(input('请选择0:ADC 1:肉盾 2:法师'))
        if number == 0:
            print('鲁班')
        if number == 1:
            print('程咬金')
        if number == 2:
            print('王昭君')
    else:
        if i != 2:
            print('输入错误,请重新输入:')
        else:
            print('已被冻结账号')
   i+=1 
