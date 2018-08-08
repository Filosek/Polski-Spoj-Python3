import sys


try:
	inputs = []
	l = [0]*10
	while True:
		inputs = list(map(str, input().split()))
		if inputs!='':
			if inputs[0] == 'z':
				l[int(inputs[1])] = int(inputs[2])
			elif inputs[0] == '+':
				print(l[int(inputs[1])]+l[int(inputs[2])])
			elif inputs[0] == '-':
				print(l[int(inputs[1])]-l[int(inputs[2])])
			elif inputs[0] == '/':
				print(int(l[int(inputs[1])]/l[int(inputs[2])]))
			elif inputs[0] == '%':
				print(l[int(inputs[1])]%l[int(inputs[2])])
			elif inputs[0] == '*':
				print(l[int(inputs[1])]*l[int(inputs[2])])
		else:
			break
		inputs.clear()
except:
	sys.exit(0)
