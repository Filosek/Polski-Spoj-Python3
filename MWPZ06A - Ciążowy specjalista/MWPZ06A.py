import sys

try:
	tests = int(input())
	for t in range(tests):
		inputs=list(map(int,input().split()))
		print(round(abs(12*((inputs[0]+inputs[1]) - (inputs[1]*inputs[2]))/(inputs[2]-1))))
except:
	sys.exit(0)