import sys

def avarageSpeed(a,b):
	return int(2*(a*b)/(a+b))

try:
	t=int(input())
	for i in range(0,t):
		y,z=map(int,input().split())
		print(avarageSpeed(y,z))

except:
	sys.exit(0)