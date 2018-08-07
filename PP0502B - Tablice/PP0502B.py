import sys

try:
	t=int(input())
	for i in range(0,t):
		number=input()
		numbers=[int(x) for x in number.split()]
		numbers.pop(0)
		numbers.reverse()
		result = ''
		for n in numbers:
			result += str(n)
			result += ' '
		print(result)
except:
	sys.exit(0)