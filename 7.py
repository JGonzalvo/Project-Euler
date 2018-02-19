prime=[2,3,5,7,11,13]

ctr=17

while 10000>prime[-1]:
	isPrime=True
	for x in prime:
		if ctr%x==0:
			isPrime=False
			break
	if isPrime:
		prime.append(ctr)
	
	ctr+=1
print(prime)

