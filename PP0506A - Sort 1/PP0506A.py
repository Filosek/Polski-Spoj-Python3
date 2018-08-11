#Another example (after FR_06_02) of frustrating problem to solve. For every kind of inputs I get correct outputs but the Judge shows me a big NOPE.
#I rewrote program in C++ that works similar to that code and it passed through judge. Don't know what is wrong with python code :/

import sys
import math
from operator import itemgetter
try:
	t=int(input())
	for i in range(0,t):
		p=int(input())
		points=[]
		for j in range(0,p):
			points.append(list(map(str, input().split())))
			points[j].append(float(math.sqrt(int(points[j][1])+int(points[j][2]))))
		points=sorted(points, key=itemgetter(3))
		for k in range(len(points)):
			print(*points[k][0:3])
		if i!=t-1:
			input()
			print()
except:
	sys.exit(0)