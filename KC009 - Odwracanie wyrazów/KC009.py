import sys
try:
	while True:
		word=str(input())
		if word!='':
			print(word[::-1])
		else:
			break
except:
	sys.exit(0)