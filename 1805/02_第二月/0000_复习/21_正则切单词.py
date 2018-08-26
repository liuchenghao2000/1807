#切单词
import re


word = 'Hello World Your So Beautiful I Love So Much'
list_1=[]
for i in (word.count(' ')+1):
	aa = re.search(r'(\w+)*',word)
	list_1.append(aa)
	print(aa)

'''
bb = word.split(' ')
print(bb)
'''
