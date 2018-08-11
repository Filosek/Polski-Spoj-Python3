import sys

try:
	t = int(input())
	for i in range(0,t):
		n=list(map(str, input().split()))
		result=''
		if(len(n[0])<=len(n[1])):
			for x in range(0,len(n[0])):
				result+=n[0][x]
				result+=n[1][x]
		elif(len(n[0])>len(n[1])):
			for x in range(0,len(n[1])):
				result+=n[0][x]
				result+=n[1][x]
		print(result)
except:
	sys.exit(0)