#匹配分组
import re
str='<html><h2>www.baidu.com</h2></html>'
#ret = re.match(r'<(?P<name1>)\w+><(?P<name2>)\w+>.*</(?P<name2>)></(?P<name1>)',str)
ret = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>',str)
print(ret)