import random
i = 0
num = random.randint(1,100)#先随机一个数字
for i in range(1,11):
    player = int(input('请输入你猜的数:'))
    if player > num:
        print('猜大了')
    elif player < num:
        print('猜小了')
    elif player == num:
        print('猜对了')
        break
