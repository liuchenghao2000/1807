#反转字符串
def all():
	name = input('输入文件名字')
	f = open(name,'w')
	f.write('123abcdefg')
	con = name.rfind('.')
	ff = open(name[0:con]+'_copy'+name[con:],'w')
	def r_string():
		book = f.rread(1)
		if ff.rread=='':
			return ''
		else:
			return ff.write(book)
			r_string()
	f.close()
	ff.close()

all()
