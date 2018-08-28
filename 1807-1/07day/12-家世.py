height = float(input('请输入身高:'))
price = float(input('请输入颜值分:'))
money = float(input('请输入身价:'))
if height > 180 and money > 1000000 and price > 99:
    print('高富帅')
elif money > 1000000 and price > 99:
    print('富帅')
elif price > 99:
    print('帅')
elif height < 160 and money < 100 and price < 60:
    print('矮穷矬')
else:
    print('非人类')

