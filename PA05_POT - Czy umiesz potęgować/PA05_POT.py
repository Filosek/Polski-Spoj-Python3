import sys

def lastPowerNum(a,b):
	modb=b%4
	if modb==1:
		return a%10
	elif modb==2:
		return (a*a)%10
	elif modb==3:
		return (a*a*a)%10
	elif modb==0:
		return (a*a*a*a)%10

try:
	d=int(input())
	for i in range(0,d):
		x,y = map(int,input().split())
		print(lastPowerNum(x,y))

except:
	sys.exit(0)