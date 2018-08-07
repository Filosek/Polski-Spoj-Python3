import sys

try:
    day=3600*24
    tests=int(input())
    for i in range(0,tests):
    	li=list(map(int, input().split()))
    	fatGuys=li[0]
    	inBox=li[1]
    	eaten=0
    	for f in range(0,fatGuys):
    		pace=int(input())
    		eaten+=int(day/pace)
    	if eaten%inBox!=0:
    		print(int(eaten/inBox)+1)
    	else:
    		print(int(eaten/inBox))

except:
	sys.exit(0)