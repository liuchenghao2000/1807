import time
import re
a=time.time()
b=re.search('\d*',str(a))
#time.sleep(5)
print('----')
c=time.time()
d=re.search('\d*',str(a))

print(d.match())
print(a) 
print(b) 
print(c) 
print(d) 