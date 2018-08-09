import sys
try:
	inputs=list(map(int, input().split()))
	t=[]
	for i in range(0,inputs[0]):
		t.append(list(map(int, input().split())))
	for i in range(0,inputs[1]):
		for j in range (0, inputs[0]):
				print(int(t[j][i]), end=' ', flush=True)
		print()
except:
	sys.exit(0)