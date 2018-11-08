import sys

try:
	while(True):
		inputs = list(map(str, input().split()))
		if inputs == "":
			break
		if(inputs[1] == "=="):
			if(int(inputs[0]) == int(inputs[2])):
				print(1)
			else:
				print(0)
		elif(inputs[1] == "<="):
			if(int(inputs[0]) <= int(inputs[2])):
				print(1)
			else:
				print(0)
		elif(inputs[1] == ">="):
			if(int(inputs[0]) >= int(inputs[2])):
				print(1)
			else:
				print(0)
		else:
			if(int(inputs[0]) != int(inputs[2])):
				print(1)
			else:
				print(0)

except:
	sys.exit()