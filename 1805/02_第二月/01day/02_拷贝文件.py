name = input('请输入要拷贝的文件')
f = open(name,'r')
c = f.read()
nu = name.rfind('.')
ff = open(name[0:nu]+'_copy'+name[nu:],'w')
ff.write(c)
 


f.close()
ff.close()