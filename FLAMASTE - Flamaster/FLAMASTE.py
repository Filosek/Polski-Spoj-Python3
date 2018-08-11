import sys

try:
	t=int(input())
	for x in range(t):
		text=str(input())
		shorter=''
		currentLetter=''
		counter=0
		for i in range(len(text)):
			if text[i]!=currentLetter:
				if counter>2:
					shorter+=currentLetter+str(counter)
				else:
					for j in range(counter):
						shorter+=currentLetter
				currentLetter=text[i]
				counter=0
			if text[i]==currentLetter:
				counter+=1
			if i+1==len(text):
				if counter>2 :
					shorter+=currentLetter+str(counter)
				else:
					for j in range(counter):
						shorter+=currentLetter
		print(shorter)
except:
    sys.exit(0)
