import sys

try:
	n=''
	toUp=False
	for line in sys.stdin:
		for w in line:
			if w!=' ':
				if(toUp):
					n+=w.upper()
					toUp=False
				else:
					n+=w
			elif w==' ':
				toUp=True
			
	print(n)
except:
    sys.exit(0)
