abundant=[]
def sum(x):
	temp=0
	for y in range(1,x//2+1):
		if x%y==0:
			temp+=y
	return temp
	
def check(target):
	if target/2 in abundant:
		return True
	for x in abundant:
		y=(target-x)
		if x>(target//2)+1:
			break
		if y in abundant:
			return True
	return False
total=0
for x in range(1,28123):
	if not check(x):
		total+=x
	if sum(x)>x:
		abundant.append(x)
	print(x)
	
print(total)