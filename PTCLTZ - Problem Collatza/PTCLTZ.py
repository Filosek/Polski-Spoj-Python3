import sys

def first_n(x, n):
	if x==1:
		return n
	elif x==0:
		return 0
	elif x%2!=0:
		return first_n(3*x+1, n=n+1)
	else:
		return first_n(x/2, n=n+1)

try:
    for i in range(0,int(input())):
    	result=0
    	print(first_n(int(input()), result))
except:
	sys.exit(0)