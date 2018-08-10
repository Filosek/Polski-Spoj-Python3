#IMPORTANT NOTE!
#Were trying to optimise, it worked but Judge said a big nope for my tries so I just cheated and used the secret power of Python

import sys

#def optimalSum(n):
#	o,t=list(map(str, n[0])),list(map(str, n[1]))
#	while len(t)<len(o):
#		t.insert(0,'0')
#	while len(t)>len(o):
#		o.insert(0,'0')
#	ans=[]
#	cache=0
#	for i in reversed(range(0,len(t))):
#		a=int(ord(o[i]) - 48)
#		b=int(ord(t[i]) - 48)
#		addition=a+b
#		if(addition>=10):
#			num=(chr(addition%10+cache+48))
#			ans.insert(0,num)
#			cache=int(addition/10)
#			if(i==0):
#				ans.insert(0,chr(cache+48))
#		else:
#			num=(chr(addition%10+cache+48))
#			ans.insert(0,num)
#			cache=0
#	ans=''.join(ans)
#	ans=ans.lstrip('0')
#	if ans=='':
#		print('0')
#	else:
#		print(ans)

try:
	for i in range(0,int(input())):
		#nums=list(map(str, input().split()))
		#optimalSum(nums)
		nums=list(map(int, input().split()))
		print(nums[1]+nums[0])
except:
	sys.exit(0)