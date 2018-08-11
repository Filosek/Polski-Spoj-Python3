import sys

try:
    First = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
             'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15}
    Second = {'A': 0, 'B': 16, 'C': 32, 'D': 48, 'E': 64, 'F': 80, 'G': 96, 'H': 112,
              'I': 128, 'J': 144, 'K': 160, 'L': 176, 'M': 192, 'N': 208, 'O': 224, 'P': 240}
    for line in sys.stdin:
    	passwd=''
    	for w in range(0,len(line)-1,2):
    		su=0
    		su+=First[line[w]]
    		su+=Second[line[w+1]]
    		passwd+=chr(su)
    	print(passwd)
except:
    sys.exit(0)
