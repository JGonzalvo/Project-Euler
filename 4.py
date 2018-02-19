x1=999
x2=999

def check(x1,x2):
	max=0
	while x1!=101:
		x2=999
		while x2!=101:
			y=x1*x2
			y2=int(str(y)[::-1])
			if y==y2:
				if y>max:
					max=y
			x2-=1
		x1-=1
	return max

z=check(x1,x2)
print(z)