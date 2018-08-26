#查手机号
import re
cc   = re.match('^1[3-9]\d{9,9}$','15225433411')
print(cc)

eml  = re.match('^\w{4,20}@126\.com$','46648@126.com')
print(eml)

word = re.match('.ui\brui\b','cui    rui')
print(word)