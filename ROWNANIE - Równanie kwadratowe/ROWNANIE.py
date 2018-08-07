import sys

try:
    while True:
    	inputs=[]
    	inputs=list(map(float, input().split()))
    	if inputs!='':
    		delta=inputs[1]**2 - (4*inputs[0]*inputs[2])
    		if delta>0:
    			print(2)
    		elif delta==0:
    			print(1)
    		else:
    			print(0)

except:
	sys.exit(0)