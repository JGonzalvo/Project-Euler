x="519432,525806"
y="632382,518061"
def isPrime(y):
	for x in range(2,y):
		if x%y==0:
			print(x)
			return False
	return True

def getGCD(x,y):
	gcd=1
	ctr=1
	while True:
		
		if(x%ctr==0 and y%ctr==0):
			gcd*=ctr
			x/=ctr
			y/=ctr
		
		if ctr>x and ctr>y:
			break
		ctr+=1
	return gcd
	
def comp(x,y):
	base1,exp1=x.split(',')
	base2,exp2=y.split(',')
	base1=int(base1)
	base2=int(base2)
	exp1=int(exp1)
	exp2=int(exp2)
	
	print(isPrime(exp1))
	
comp(x,y)