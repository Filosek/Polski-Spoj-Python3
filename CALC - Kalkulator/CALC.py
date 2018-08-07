import sys

try:
	while True:
		inputs=list(map(str, input().split()))
		if inputs!='':
			if (inputs[0]=='+'):
				print(int(inputs[1])+int(inputs[2]))
			elif (inputs[0]=='-'):
				print(int(inputs[1])-int(inputs[2]))
			elif (inputs[0]=='*'):
				print(int(inputs[1])*int(inputs[2]))
			elif (inputs[0]=='/'):
				print(int(int(inputs[1])/int(inputs[2])))
			elif (inputs[0]=='%'):
				print(int(inputs[1])%int(inputs[2]))
			else:
				break
except:
	sys.exit(0)