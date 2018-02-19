x=2000000

def check(x):
	sum=0
	for temp in list(str(x)):
		sum+=int(temp)**5
	return sum
sum=0
for temp in range(0,x):
	if check(temp) ==temp and len(str(temp))>2:
		print(temp)
		sum+=temp
		
print(sum)