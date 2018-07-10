#名片系统

import os
def beifen():
		name == input('输入需备份的文件名')
		file_1 = open(name,'r')
		file_2 = open([0:name.rfind('.')]+'_copy'+[name.rfind('.'):],'w')
		while True:
			inf = file_1.read(1024)
			file_2.write(inf)
			if inf=='':
				print('备份完成')
				file_1.close()
				file_2.close()
				break

card = []
while True:
	print('1.增\n2.查\n3.改\n4.删\n5.备份\n6.批量命名\n7.读取\n8.写入')
	main_o == input('请输入选项')
#备份
	if main_o == '5':
		beifen()
	elif main_o == '6':
		dir_name == input('输入文件夹名字')
		files = os,listdir(dir_name)
		for file in files:
			old_file = dir_name+ '/' +file
			new_file = dir_name+ '/' +file
			os.rename(old_file,new_file)
:
	elif main_o == '7':
	elif main_o == '8':


