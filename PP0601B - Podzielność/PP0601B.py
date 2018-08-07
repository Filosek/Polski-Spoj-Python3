import sys

def divisibleNums(n,x,y):
	divisibles=[]
	for i in range(x,n):
		if i%x==0 and i%y!=0:
			divisibles.append(i)
	print(*divisibles)

try:
    tests=int(input())
    for i in range(0,tests):
    	inputs=list(map(int,input().split()))
    	divisibleNums(inputs[0], inputs[1], inputs[2])

except:
	sys.exit(0)