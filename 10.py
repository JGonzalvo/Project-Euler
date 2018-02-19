import math
prime=[2,3]

ctr=5

while 2000000>prime[-1]:
	isPrime=True

	max=int(math.sqrt(prime[-1]))+1
	for x in prime:
		if ctr%x==0:
			isPrime=False
			break
		if x>max:
			break

	if isPrime:
		prime.append(ctr)
		print(prime[-1])
	ctr+=2
	
print(sum(prime[:-1]))

