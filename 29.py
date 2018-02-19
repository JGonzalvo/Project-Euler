temp=[]

for a in range(2,101):
	for b in range(2,101):
		temp.append(a**b)

print(len(temp),len(set(temp)))

