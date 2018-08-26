name = input('请输入要备份的文件名')
f = open(name,'r')
content = f.read()

a = name.rfind('.')
c = name[:a]+'备份'+name[a:] 



f1 = open(c,'w')
f1.write(content)


f.close()
f1.close()
