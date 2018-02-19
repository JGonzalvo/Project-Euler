x=600851475143
ctr=2
while x!=1:
	if x%ctr==0:
		x/=ctr
		print(ctr)
	ctr+=1