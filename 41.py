import math

digits=[True]*999999999
digits[0]=False
digits[1]=False


max=math.sqrt(len(digits))

for x in range(2,int(max)+1):
	for y in range(x,x*len(digits)//x,x):
		digits[y]=False
	digits[x]=True
print(digits)


for index, item in enumerate(digits):
	if(item):
		print(index)

		