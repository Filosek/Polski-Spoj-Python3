import sys


try:
	while True:
		inputs=list(map(str, input().split()))
		counter=0
		if inputs!='':
			for i in range(2, len(inputs)):
				if inputs[i] == inputs[0]:
					counter+=1
		else:
			break
		print(counter)
except:
	sys.exit(0)