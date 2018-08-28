while True:
    import random

    player = int(input('请出拳1,石头2,剪刀3,布'))
    pc = random.randint(1,3)
    if player < 4 and player > 0:
        if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
            print('对面弱爆了')
        elif player == pc:
            print('再来,再来')
        else:
            print('对面很强啊')
    else: 
        print('输入不合法')
