import sys

try:
	while True:
		text=list(map(str, input()))
		if text !='':
			for l in range(0,len(text)):
				if text[l]==' ' or text[l]=='\n':
					continue
				elif text[l]=='X' or text[l]=='Y' or text[l]=='Z':
					text[l]=chr(ord(text[l])-23 )
				else:
					text[l]=chr(ord(text[l])+3)
			text=''.join(text)
			print(text)
			text=''
		else:
			break
except:
	sys.exit(0)