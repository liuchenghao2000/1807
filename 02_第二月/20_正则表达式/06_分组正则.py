#查html
import re
wed = "<1><2>asafs</2></1>"

test = re.match('<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?P=name1)>',wed)
print(test)