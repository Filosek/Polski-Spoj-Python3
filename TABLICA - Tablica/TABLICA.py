import sys

try:
    n=list(map(int, input().split()))
    print(*n[::-1])
except:
	sys.exit(0)