import os
dir = input("请输入批量重命名的文件夹名字:")
files = os.listdir(dir)#列表
os.chdir(dir)

for i in files:
    position = i.rfind('.')
    newname = i[:position]+'-腾讯'+i[position:]
    oldname = dir+'/'+i
    newmame = dir+'/'+newname
    os.rename(i,newname)

