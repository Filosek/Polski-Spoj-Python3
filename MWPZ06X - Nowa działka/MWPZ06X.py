import sys

try:
    D=int(input())
    for i in range(0,D):
    	x=int(input())
    	print(x**2)
except:
	sys.exit(0)