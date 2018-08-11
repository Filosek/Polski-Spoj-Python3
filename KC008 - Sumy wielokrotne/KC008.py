import sys

try:
	result = 0
	for line in sys.stdin:
		n = list(map(int,line.split()))
		nsum = sum(n)
		result += nsum
		print(nsum)
	print(result)
except:
    sys.exit(0)
