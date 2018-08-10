import sys

try:
	a=[]
	while True:
		n=str(input())
		if n!='':
			if n=='+':
				if len(a)<10:
					a.insert(0,int(input()))
					print(':)')
				else:
					print(':(')
			elif n=='-':
				if not a:
					print(':(')
				else:
					print(a[0])
					a.pop(0)
		else:
			break
except:
	sys.exit(0)