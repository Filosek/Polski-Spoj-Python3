import sys

try:
    inputs = list(map(int, input().split()))
    tab = list(map(int, input().split()))
    for i in range(0, inputs[1]):
    	tab+=[tab.pop(0)]
    print(*tab)
except:
	sys.exit(0)