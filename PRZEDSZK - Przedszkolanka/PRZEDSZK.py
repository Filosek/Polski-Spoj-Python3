import sys

def GCD(a,b):
	if a==0 and b!=0:
		return b;
	elif a!=0 and b==0:
		return a;
	return GCD(b, a%b)


def LCM(a,b):
	return int((a*b)/GCD(a,b))

try:
	N = int(input())
	for x in range(0,N):
		a,b = map(int, input().split())
		print(LCM(a,b))

except:
	sys.exit(0)