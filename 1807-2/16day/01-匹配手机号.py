import re
phone = input('请输入手机号:')
def phone_a():
	ret = re.match(r'1[3456789]\d{9}$',phone)
	if ret:
		print('合法')
	else:
		print('不合法')	

phone_a()
