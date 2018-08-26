height = float(input('请输入身高:'))
weight = float(input('请输入体重:'))
bml = weight/height**2
if bml < 18.5:
    print('过轻')
elif bml > 18.5 and bml < 25:
    print('正常')
elif bml > 25 and bml < 28:
    print('过重')
elif bml > 28 and bml < 32:
    print('肥胖')
else:
    print('严重肥胖') 
