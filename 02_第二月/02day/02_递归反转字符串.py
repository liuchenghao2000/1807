str_=input('请输入任意字符串')
def r_sing(x):
	if x== -1:
		return ''
	else:
		return str_[x] + r_sing(x-1)

print(r_sing(len(str_) - 1))
