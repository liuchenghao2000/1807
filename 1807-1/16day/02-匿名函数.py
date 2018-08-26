def clum(x,y,z):
    #print(z)#打印匿名地址
    ret = z(x,y)
    return ret
#ret = clum(1,2,lambda x,y:x+y)
#print(ret)
#print(clum)#打印函数地址
ret = clum(1,2,lambda x,y:x-y)
print(ret)




