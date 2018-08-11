import sys

try:
	while True:
		n=list(map(str,input().split()))
		if n!='':
			text=''
			for a in n[1]:
				if a!=n[0]:
					text+=a
			print(text)
		else:
			break
except:
	sys.exit(0)