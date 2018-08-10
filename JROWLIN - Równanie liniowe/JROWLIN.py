import sys

def linear(a,b,c):
	b-=c
	if a==0 and b!=0:
		print('BR')
	if a==0 and b==0:
		print('NWR')
	if a!=0:
		print('{:.2f}'.format(round(-b/a,2)))


try:
	inputs=list(map(float,input().split()))
	linear(inputs[0],inputs[1],inputs[2])
except:
	sys.exit(0)