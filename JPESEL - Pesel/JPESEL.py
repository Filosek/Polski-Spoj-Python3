import sys

def check(a):
	for n in range(0,len(a)):
		if n==1 or n==5 or n==9:
			a[n]*=3
		elif n==2 or n==6:
			a[n]*=7
		elif n==3 or n==7:
			a[n]*=9
	if sum(a)%10==0:
		print('D')
	else:
		print('N')

try:
    tests = int(input())
    for i in range(0,tests):
    	pesel=str(input())
    	ints=[]
    	for n in pesel:
    		ints.append(int(n))
    	check(ints)
except:
	sys.exit(0)