import sys
import string

try:
	uppercase=string.ascii_uppercase
	lowercase=string.ascii_lowercase
	alphabet=lowercase+uppercase
	t=int(input())
	text=''
	for line in sys.stdin:
		text+=line
	for l in alphabet:
		counter=0
		for w in text:
			if l==w:
				counter+=1
		if counter!=0:
			print(l,counter)
except:
	sys.exit(0)