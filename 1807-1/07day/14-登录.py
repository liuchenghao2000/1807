account = 123456
password = 'abc'
a = int(input('请输入账号:'))
p = input('请输入密码:')
if a == account and p == password:
    print('登陆成功')
elif a != account:
    print('账号不对')
elif p != password:
    print('密码错误')
