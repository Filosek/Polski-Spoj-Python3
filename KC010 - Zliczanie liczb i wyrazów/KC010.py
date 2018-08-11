import sys

def is_number(w):
	try:
		int(w)
		return True
	except ValueError:
		return False

try:
	for lines in sys.stdin:
		nums=0
		words=0
		l=list(map(str,lines.split()))
		for w in range(len(l)):
			if is_number(l[w]):
				nums+=1
			else:
				words+=1
		print(nums,words)

except:
    sys.exit(0)
