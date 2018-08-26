class BeiFen:
    def beifen(self):
        name = input('请输入要备份的文件名')
        f = open(name,'r')
        a = name.rfind('.')
        c = name[:a]+'备份'+name[a:] 
        f1 = open(c,'w')
        while True:
            content = f.read(1024)
            f1.write(content)
            if len(content) == 0:
                break


        f.close()
        f1.close()

lad = BeiFen()
lad.beifen()


