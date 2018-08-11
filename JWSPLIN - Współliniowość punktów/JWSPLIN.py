import sys

def collinearity(xa,ya,xb,yb,xc,yc):
	if xb-xa==0:
		aAB=0
	else:
		aAB=(yb-ya)/(xb-xa)
	if xc-xb==0:
		aBC=0
	else:
		aBC=(yc-yb)/(xc-xb)
	if aAB==aBC:
		print('TAK')
	else:
		print('NIE')

try:
	t=int(input())
	for i in range(0,t):
		n=list(map(int,input().split()))
		collinearity(n[0],n[1],n[2],n[3],n[4],n[5])
except:
	sys.exit(0)