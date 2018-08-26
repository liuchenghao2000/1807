#
import re
web = 'https:\\www.facebook.com.dasfase'

#test = re.match('http(|s)\:\\\\www\.\w+\.com.*',web)
test = re.sub('[(http(|s)\:\\\\www\.\w+\.com$)]','',web)

print(test)
