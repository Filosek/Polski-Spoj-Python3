import sys

try:
	first=True
	past=0
	counter=0
	while True:
		current=int(input())
		print(current)
		if current==42 and past!=42 and not first:
			counter+=1
		if counter==3:
			break
		past=current
		first=False
except:
	sys.exit(0)