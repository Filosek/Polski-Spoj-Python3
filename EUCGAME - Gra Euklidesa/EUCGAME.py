import sys

def GCD(a,b):
	if a==0 and b!=0:
		return b;
	elif a!=0 and b==0:
		return a;
	return GCD(b, a%b)

def game(a,b):
	return GCD(a,b)*2


try:
    t=int(input())
    for i in range(0,t):
    	inputs=list(map(int, input().split()))
    	print(game(inputs[0],inputs[1]))
except:
	sys.exit(0)