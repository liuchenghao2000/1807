import random

pc = random.randint(1,100)
for i in range(10):
    player = int(input('请输入数字:'))
    if player > pc:
        print('太大了')
    elif player < pc:
        print('太小了')
    else:
        print('答对了')
        break








