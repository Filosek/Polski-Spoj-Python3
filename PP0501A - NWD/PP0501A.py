import sys

def GCD(a,b):
	if a==0 and b!=0:
		return b;
	elif a!=0 and b==0:
		return a;
	return GCD(b, a%b)


try:
	n=int(input())
	for x in range(0,n):
		y, z = map(int,input().split())
		print(GCD(y,z))	

except:
	sys.exit(0)