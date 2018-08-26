def line_conf(a,b):
	def line(x):
		return a*x+b
	return line

line = line_conf(2,3)
print(line(5))
print(line(6))
print(line(7))

def line(a,b,x):
	return a*x+b
line(2,3,5)
line(2,3,6)
line(2,3,7)