import sys

try:
	t = int(input())
	for i in range (0, t):
		n=list(map(str, input().split()))
		counter=n[1].count('?')
		result=1
		if counter==0:
			print('1')
		elif counter==1 and len(n[1])==1:
			print('10')
		elif n[1][0]=='?':
			result*=9
			result*=10**(counter-1)
			print(result)
		else:
			result*=10**(counter)
			print(result)
except:
	sys.exit(0)