import sys

def chSystem(a,b):
	newsigns = {0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
	ans=''
	if a==0:
		return '0'
	while a!=0:
		new=a%b
		ans+=newsigns[int(new)]
		a=int(a/b)
	ans=ans[::-1]
	return ans
	
try:
	t=int(input())
	for i in range(t):
		a=int(input())
		print(chSystem(a,16),chSystem(a,11))
except:
    sys.exit(0)
