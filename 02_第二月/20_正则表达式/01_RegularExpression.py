#导入re模块
import re
#使用match方法进行匹配
#re.match('正则表达式','要匹配的字符串')
result = re.match('baidu','baidu.com')
#如果上一句匹配到数据，可以使用group方法提取数据
print(result.group())
