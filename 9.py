import math
a=1
b=1
c=1
max=334
while True:
	c=int(math.sqrt(a**2+b**2))
	
	
	if(c**2==a**2+b**2) and a+b+c==1000:
		print(a*b*c)
		break
	if a>max:
		a=1
		b+=1
	a+=1