x1=100


sum1=0
for x in range(0,x1+1):
	sum1+=x


sum2=0
for x in range(0,x1+1):
	sum2+=x**2
	
print(sum1**2-sum2)