#lambda
y=lambda a:a+4
print(y(3))

z=lambda a,b,c,d=3:(a**b+c)%d
print(z(3,4,5))

x= lambda a,b,c: a*b*c
print(x(-1,3,-1))
#a=4
l=[lambda a:a**2,lambda a:a**3,lambda a:a**4]
print((l[0](2),l[1](2),l[2](2))