import sys

try:
    t = int(input())
    for i in range(0,t):
    	word=str(input())
    	print(word[:-int(len(word)/2)])
except:
	sys.exit(0)