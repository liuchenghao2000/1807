import re
mile = input('请输入邮箱:')
def a():
	ret = re.match('^\w{4,20}@(qq|163|wangyi|126)\.com',mile)
	if ret:
		print('合法')
	else:
		print('不合法')


a()