import sys

def couldHandle(c,k,w):
	if(w*c<=k):
		print('yes')
	else:
		print('no')


try:
	t=int(input())
	for i in range(0,t):
		inputs=list(map(int, input().split()))
		couldHandle(inputs[0],inputs[1],inputs[2])
except:
	sys.exit(0)