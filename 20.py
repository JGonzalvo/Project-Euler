n=100

def fact(x):
	if x==1:
		return 1
	else:
		return x*fact(x-1)
		
x=list(str(fact(n)))
sum=0
for y in x:
	sum+=int(y)
	
print(sum)