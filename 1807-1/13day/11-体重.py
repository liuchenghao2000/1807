l = float(input('请输入身高:'))
w = float(input('请输入体重:'))
b = w/l**2
if b < 18.5:
    print('过轻')
elif b >= 18.5 and b < 25:
    print('正常')
elif b >= 25 and b < 28:
    print('过重')
elif b >= 28 and b < 32:
    print('肥胖')
else:
    print('严重肥胖')



