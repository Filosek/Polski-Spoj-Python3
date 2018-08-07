import sys

def evenOdd(a):
	sorted=[]
	for n in range(0,len(a)):
		if n%2==1:
			sorted.append(a[n])
	for n in range(0,len(a)):
		if n%2!=1:
			sorted.append(a[n])
	print(*sorted)

try:
    tests = int(input())
    for i in range(0,tests):
    	inputs=list(map(int, input().split()))
    	inputs.pop(0)
    	evenOdd(inputs)
except:
	sys.exit(0)