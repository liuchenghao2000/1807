#文件复习使用

#创写文件
f=open('1.txt','w')
i='x+y=10\nx-2y=4\n'
f.write(i)
f.close()

#追加文件
ff=open('1.txt','a')
u='x=8\ny=2\n'
ff.write(u)
ff.close()

#读文件定向
file_1=open('1.txt','r')
file_2=open('2_test.txt','w')

aal = file_1.read()
file_2.write(aal)
file_1.close()
file_2.close()

#读文件追加
file_3=open('3_test.txt','a')
file_1=open('1.txt','r')
aa=file_1.read()
file_2=open('2_test.txt','r')
bb=file_2.read()
file_3.write(aa)
file_3.write(bb)
file_1.close()
file_2.close()
file_3.close()

#批量重命名

'''
import os

dir_name=os.getcwd()
files = os.listdir(dir_name)
for file in files:
	old_fname=dir_name+'/'+file
	new_fname=dir_name+'/'+'精品'+file
	os.rename(old_fname,new_fname)
'''