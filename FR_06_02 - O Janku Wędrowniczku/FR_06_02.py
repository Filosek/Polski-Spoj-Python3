#Tried clever usage of str.count(''), worked for example from SPOJ and for my own data, but didn's pass through the judge
#Tried this algorithm (I used it in passed through code wrote in C++) but this also didn't pass through the judge :/
#I don't want to create the repository for SPOJ solved problems in C++ so here i found other users code in C++ similar to mine: 
#https://github.com/romic96/spoj/blob/master/%5B1%5D%20FR_06_02%20-%20O%20Janku%20W%C4%99drowniczku.cpp
#Really sometimes I think that Judge just hate python :( Were writing in C++ for my whole programming life and now just wanted to learn some other
#language but I feel rolled off by Judge
#Every of mine friends says that Python is the easiest to use language with many built in functions but really I'm just having so much fun using it
#FunFact: Nobody solved that problem with Python3.5 on SPOJ

#First method (Similar to C++)
import sys

try:
	counter=0
	suspensions=0
	for line in sys.stdin:
		for w in range(0,len(line)):
			if line[w]=='?':
				counter+=1
			elif line[w]=='!':
				counter+=1
			elif line[w]=='.':
				if w+2<len(line) and line[w+2]=='.':
					counter+=1
					suspensions+=1
				else:
					counter+=1
	counter-=suspensions*2
	print(counter)
except:
	sys.exit(0)

#Second method (Python way)
#import sys
#try:
#	counter=0
#	for line in sys.stdin:
#		counter+=line.count('!')
#		counter+=line.count('?')
#		counter+=line.count('.')
#		duals=line.count('..')
#		suspensions=line.count('...')
#		for i in range(0,suspensions):
#			counter-=2
#	print(counter)
#except:
#	sys.exit(0)