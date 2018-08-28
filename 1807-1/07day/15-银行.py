account = 'lch'
password = '2000'
money = 1000
a = input('请输入账号:')
p = input('请输入密码:')
if a == account and p == password:
    print('请取钱')
    m = float(input('请输入取钱金额:'))
    m1 = money-m
    if m > 1000:
        print('余额不足')
    elif m < 1000:
        print('取了%.02f,还剩%.02f'%(m,m1))
else:
    print('非法账户') 
