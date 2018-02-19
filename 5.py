max=20
temp=[]
for x in range(1,max):
	temp.append(x)
	
for pos in range(0,max-1):
	for itr in range(pos+1,max-1):
		if temp[itr]%temp[pos]==0 and itr!=pos:
			temp[itr]/=temp[pos]
total=1		
for x in temp:
	total*=int(x)
	
print(total)