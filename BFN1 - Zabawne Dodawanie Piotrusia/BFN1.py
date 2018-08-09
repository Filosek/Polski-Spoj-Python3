import sys

try:
	t=int(input())
	for i in range(0,t):
		n=str(input())
		counter=0
		if n==n[::-1]:
			print('%s %s' % (n, counter))
		else: 
			while n!=n[::-1]:
				counter+=1
				n,no=int(n), int(n[::-1])
				n+=no
				n=str(n)
			print ('%s %s' % (n, counter))
except:
	sys.exit(0)