import sys

try:
	A=False
	for line in sys.stdin:
		fixed=list(map(str,line))
		for w in range(0, len(fixed)):
			if(fixed[w]=='<'):
				A=True
			elif(fixed[w]=='>'):
				A=False
			if(A):
				fixed[w]=str(fixed[w]).upper()
		fixed=''.join(fixed)
		print(fixed)
except:
	sys.exit(0)