import re

num = '<html><h1>dsfg</h1></html>'
ret = re.match('<(?P<name1>\w+)><(?P<name2>\w+)>.+</(?P=name2)></(?P=name1)>',num)

print(ret)