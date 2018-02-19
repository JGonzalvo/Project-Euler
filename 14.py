
def getCollatz(x):
	ctr=0
	while x!=1:
		if x%2==0:
			x=x//2
		else:
			x=3*x+1
		ctr+=1
	return ctr
		
max=0
goal=0
for x in range(1000000,0,-1):
	temp=getCollatz(x)
	if temp>max:
		max=temp
		goal=x
		
print(goal,max)
