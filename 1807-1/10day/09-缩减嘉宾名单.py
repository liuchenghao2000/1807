list = ['马晨浩','毛泽东','杨昕义','习近平','奥巴马','李军']
list1 = ['马晨浩','毛泽东','杨昕义','奥巴马']
for j in list1:
    print('%s,由于本人原因未能邀请您,深表歉意'%j)    
list.pop(0)
list.pop(0)
list.pop(0)
list.pop(1)
for i in list:
    print('%s您仍是受邀人'%i)

del list[0]
del list[0]
print(list)
