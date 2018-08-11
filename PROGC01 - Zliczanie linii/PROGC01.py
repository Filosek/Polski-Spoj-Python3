import sys

try:
	counter=0
	for line in sys.stdin:
		counter+=1
	print(counter)
except:
	sys.exit(0)