prime=[2,3,5,7,11,13]

ctr=17
def check(x,y):
	x=list(str(x))
	x.sort()
	y=list(str(y))
	y.sort()
	
	if x==y:
		return(True)
	else:
		return(False)

while 10000>prime[-1]:
	isPrime=True
	for x in prime:
		if ctr%x==0:
			isPrime=False
			break
	if isPrime:
		prime.append(ctr)
	ctr+=1

def eval(start):
	for x in range(start,len(prime)):
		for y in range(x+1,len(prime)):
			if check(prime[x],prime[y]) and x!=y:
				for z in range(y+1,len(prime)):
					if check(prime[y],prime[z]) and y!=z and prime[y]-prime[x]==prime[z]-prime[y]:
						print(prime[x],prime[y],prime[z])
				break
			
eval(0)