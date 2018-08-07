import sys

try:
    try:
    	result=0
    	while True:
    		x = int(input())
    		if x!="":
    			result+=x
    			print(result)
    		else:
    			break
    except EOFError:
    	pass
except:
	sys.exit(0)