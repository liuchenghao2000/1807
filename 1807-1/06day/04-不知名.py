name = input("请输入名字:")
age = input("请输入年龄:")
sex = input("请输入性别:")
height = input("请输入身高:")
#print(name,age,sex)

'''
print(name)
print(age)
print(sex)
把自己的个人信息输入进来要整数 要有浮点数 要有字符格式 格式化输出到屏幕上
'''

#格式化输出
#%s 占位符字符
#%f 占位符点数 保留两位小数%.02f
#%d 占位整数
print("我的名字是%s,我的年龄是%f,我的性别是%d,我的身高是%0.2f"%(name,age,sex,height))

