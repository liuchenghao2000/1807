for i in range(1,10):
	for j in range(i):
		print('  %d*%d=%d'%(j,i,j*i),end='')
		j+=1
	print('\n')
	
