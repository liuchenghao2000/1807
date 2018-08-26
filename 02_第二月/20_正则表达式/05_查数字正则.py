#数字
import re
#num ='010'  #重点测试 0 00 000
num ='45.6846'
l = []
#按照位数		可以
#test = re.match('((00[1-9]]|0[1-9]\d|100)|(0[1-9]|[1-9]\d)|[1-9])$',num)
#按照排除零	不可行
#test = re.match('([^0*])$',num)
#test = re.match('(0*\d{1,2})$',num)
#按照  拼数  0部分 与数部分		成功
#					一位		两位		三位			小数
#test = re.match('((0*[1-9])|0*[1-9]\d|0*100)$',num)
test = re.match('(((0{,2}[1-9])|0{,1}[1-9]\d)(\.\d*)*|100)$',num)
#以上拼数简化
#test = re.match('(0*[1-9]\d{,1}|100)$',num)
l.append(test)
print(l)
print(test)