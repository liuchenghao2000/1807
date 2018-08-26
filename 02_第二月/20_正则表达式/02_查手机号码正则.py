#手机号
import re
tel='15225433411'

over=re.match('1[3-9]\d{9}$',tel)
print(over)