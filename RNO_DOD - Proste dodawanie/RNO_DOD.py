import sys
try:
	sum_count=int(input())
	for x in range(0,sum_count):
		numbers_count=int(input())
		numbers = input()
		wholeSum=sum([int(x) for x in numbers.split()])
		print(wholeSum)

except:
	sys.exit(0)
	