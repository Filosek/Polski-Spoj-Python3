import sys

try:
    inputs=list(map(float, input().split()))
    print((inputs[0]**2 - ((inputs[1]**2)/4))*3.141592654)
except:
	sys.exit(0)