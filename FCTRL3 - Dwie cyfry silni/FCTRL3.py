import sys
def factorial(n):
	if n<=1:
		return 1
	elif n>9:
		return 100
	else:
		result=1
		for a in range(2,n+1):
			result*=a
		return result

try:
	d = int(input())
	for x in range(0,d):
		number=int(input())
		print("{} {}".format(int((factorial(number)%100)/10),factorial(number)%10))
except:
	sys.exit(0)