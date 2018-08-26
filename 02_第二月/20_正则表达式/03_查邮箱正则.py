#检查邮箱
import re


eml='234dasdasdsadww@126.com'
test = re.match('^\w{4,20}@(qq|163|wangyi|126)\.com',eml)
print(test)
