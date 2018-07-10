print('房屋类型别墅型\n大户型\n小户型\n胶囊型')
print()
a = input('请输入房子大小____')
print()
print('540,280,140,70,20')
print()
b = float(input('请输入房子面积____㎡'))
print()
print('北京，上海，广东，西安，洛阳，哈尔滨，昆明，乌鲁木齐，台北')
c = input('请输入所处城市————')
print()
print('老城区，开发区，新区')
d = input('请输入详细位置————')
e = float(input('请输入价格预算————万元'))
print()
print('小张，小李，小赵，小马，小王')
input('购买顾问是谁')


#***************************************
if   c == '北京' or c == '上海' or c == '广东':
	if   d =='老城区':
		x = float(8)  #8万元
	elif d =='开发区':
		x = float(4)  #4万元
	elif d =='新区':
		x = float(2)  #2万元
elif c == '西安' or c == '哈尔滨' or c == '洛阳':
	if   d =='老城区':
		x = float(2)  #2万元
	elif d =='开发区':
		x = float(1)  #1万元
	elif d =='新区':
		x = float(0.7)#0.7万元
elif c == '昆明' or c == '台北' or c ==  '乌鲁木齐':
	if   d =='老城区':
		x = float(1.5)
	elif d =='开发区':
		x = float(1)
	elif d =='新区':
		x = float(0.6)
z = x * b
y = e - z
#×××××××××××××××××××××××××××××××××××××××


print('-'*50)
print('您的户型为%s'%a)
print('您的房屋面积为%d㎡'%b)
print('你房屋所在城市是%s'%c)
print('您房屋的详细位置在%s'%d)
print('-'*50)
print()
print()
print()
print('您房屋每㎡价格为%.02f万元'%x)
print()
print('价格预算:%.02f 万元'%e)
print()
print('-'*50)
print('此房屋总价为:%.02f 万元'%z)
print()
print('还有差价:%.02f 万元'%y)

print('-'*50)
