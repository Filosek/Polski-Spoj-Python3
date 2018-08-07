import sys
from collections import deque

try:
    t=int(input())
    for i in range(0,t):
    	li=list(map(int, input().split()))
    	li.pop(0)
    	li = deque(li)
    	li.rotate(-1)
    	print(*li)
except:
	sys.exit(0)