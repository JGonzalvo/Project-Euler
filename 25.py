fib=[1,1,2]

ctr=3
while len(str(fib[2]))!=1000:
	fib.pop(0)
	fib.append(sum(fib))
	ctr+=1
print(ctr)