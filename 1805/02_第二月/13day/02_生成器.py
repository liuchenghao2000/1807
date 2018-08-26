# 生成器
l=(x for x in range(100) if x%13==0)

print(next(l))

for i in l:
	print(next(l))