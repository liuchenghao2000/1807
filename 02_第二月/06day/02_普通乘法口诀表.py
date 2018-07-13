for i in range(1,10):
	for u in range(1,10):
		if u<=i:
			print('%d*%d=%d'%(i,u,(i*u)),end='\t')
	print('')