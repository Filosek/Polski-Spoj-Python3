import sys

try:
	t=int(input())
	for i in range(0,t):
		e=int(input())
		vertically=0
		horizontally=0
		for j in range(0,e):
			data=list(map(int, input().split()))
			if data[0]==0:
				vertically+=data[1]
			elif data[0]==1:
				vertically-=data[1]
			elif data[0]==2:
				horizontally+=data[1]
			elif data[0]==3:
				horizontally-=data[1]
		if vertically==0 and horizontally==0:
			print('studnia')
		if vertically>0:
			print('0',vertically)
		elif vertically<0:
			print('1',abs(vertically))
		if horizontally>0:
			print('2',horizontally)
		elif horizontally<0:
			print('3',abs(horizontally))
except:
	sys.exit(0)