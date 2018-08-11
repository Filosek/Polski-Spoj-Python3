import sys

try:
	t=int(input())
	for i in range(0,t):
		n=list(map(float, input().split()))
		n.pop(0)
		avg=sum(n)/len(n)
		x=abs(avg-n[0])
		closest=x
		number=n[0]
		for a in n:
			x=abs(avg-a)
			if(x<closest):
				closest=x
				number=a

		print(int(number))

except:
	sys.exit(0)