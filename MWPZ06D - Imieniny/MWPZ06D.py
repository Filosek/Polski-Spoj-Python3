import sys

try:
	t=int(input())
	for i in range(0, t):
		a=list(map(int,input().split()))
		a[0]-=1
		if a[0]==0:
			print('TAK')
		elif a[1]%a[0]!=0:
			print('TAK')
		elif a[1]%a[0]==0:
			print('NIE')
except:
	sys.exit(0)