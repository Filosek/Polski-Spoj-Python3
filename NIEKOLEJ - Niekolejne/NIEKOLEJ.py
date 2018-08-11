import sys

try:
	n=int(input())
	nums=list(range(n+1))
	newNums=[]
	if n == 0:
		print('0')
	elif n == 2 or n == 1:
		print('NIE')
	else:
		for n in range(1,len(nums),2):
			newNums.append(n)
		for n in range(0,len(nums),2):
			newNums.append(n)
		print(*newNums)


except:
    sys.exit(0)
