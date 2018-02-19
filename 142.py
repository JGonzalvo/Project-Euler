import time
start_time = time.time()
import math
def isSquare(x):
	return int(math.sqrt(x))**2==x
	
def main():
	
	a=1
	while True:
		A=a**2
		for f in range(1,a):
			if isSquare(A-(f**2)):
				F=f**2
				C=A-F
				if not isSquare(C):
					break
				c=math.sqrt(C)
				#Assumption C>E
				for d in range(f+1,int(c)):
					if isSquare(A-(d**2)):
						D=d**2
						if (C+D)%2 != 0:
							break
						E=A-D
						if (E+F)%2 != 0:
							break
						if isSquare(E):
							print("FOUND")
							B=C-E
							if isSquare(B):
								print(A,B,C,D,E,F)
								x=(C+D)//2
								print(x,A-x,C-x)
								quit()
		a+=1
main()
print("--- %s seconds ---" % (time.time() - start_time))