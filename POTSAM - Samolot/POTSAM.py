import sys

try:
    n1,k1,n2,k2=map(int,input().split())
    print((n1*k1)+(n2*k2))
except:
	sys.exit(0)