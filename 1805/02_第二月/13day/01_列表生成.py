l=[x for x in range(10)]
print(l)

ll=[(x,y) for x in range(100) if x%13==0 for y in range(100) if y%29==0]
print(ll)