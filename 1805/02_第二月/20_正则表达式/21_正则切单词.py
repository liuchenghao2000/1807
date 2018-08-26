#切单词
import re


word = 'Hello World Your So Beautiful I Love So Much'
list_1=[]

aa = re.search(r'(\S+){0,}',word)
print(aa)

'''
bb = word.split(' ')
print(bb)
'''
