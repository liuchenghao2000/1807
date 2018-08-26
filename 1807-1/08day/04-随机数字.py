import random
i = 0
num = random.randint(1,100)#先随机一个数字
while i < 9:
    u_num = int(input('请输入数字'))
    if u_num > num:
        print('你猜大了')
    elif u_num < num:
        print('你猜小了')
    else:
        print('猜对了')
        break
    i+=1
