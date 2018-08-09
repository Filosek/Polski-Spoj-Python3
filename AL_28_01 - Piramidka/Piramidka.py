import sys

try:
	length = int(input())
	word = list(input())
	center = int((length-1)/2)
	new_word = list(['.']*length)
	for i in range(0, center+1):
		new_word[center-i]=word[center-i]
		new_word[center+i]=word[center+i]
		print(*new_word, sep='')
except:
	sys.exit(0)
