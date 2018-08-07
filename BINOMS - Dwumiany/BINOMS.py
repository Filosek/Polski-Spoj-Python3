import sys

def Factorial(N):
	product = 1
	for j in range(1,N+1):
		product*=j
	return product

def Newton(n,k):
	result = 1;
	if n==k:
		return 1
	if k==0:
		return 1
	for i in range(0,k):
		result*=n-i
	return int(result / Factorial(k))

try:
	tests = int(input())
	for i in range(0,tests):
		a,b=map(int,input().split())
		if a==b:
			print(1)
		else:
			print(Newton(a,b))
except:
	sys.exit(0)