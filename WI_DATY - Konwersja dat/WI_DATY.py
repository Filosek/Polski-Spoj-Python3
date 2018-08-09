#I finished my code then realised that It's not for Python :cryingRiver: 


import sys

def ToISO(a):
	year=1980
	month=0
	day=0
	for i in reversed(range(0,7)):
		if a[i]=='1':
			year+=2**(6-i)
	for i in reversed(range(7,11)):
		if a[i]=='1':
			month+=2**(10-i)
	for i in reversed(range(11,16)):
		if a[i]=='1':
			day+=2**(15-i)
	if year>=1980 and year<2107 and day>0 and day<=31 and month>0 and month<=12:
		print('%s-%s-%s' % (year, month, day))
	else:
		print('ERROR')

def ToDOSFAT(a):
	year=list(map(int,date[0:4]))
	month=list(map(int,date[5:7]))
	day=list(map(int,date[8:10]))
	year=year[0]*1000+year[1]*100+year[2]*10+year[3]
	month=month[0]*10+month[1]
	day=day[0]*10+day[1]
	if year>=1980 and year<2107 and day>0 and day<=31 and month>0 and month<=12:
		year-=1980
		year='{0:07b}'.format(year)
		month='{0:04b}'.format(month)
		day='{0:05b}'.format(day)
		year+=month
		year+=day
		print(year)
	else:
		print('ERROR')

try:
	date=list(map(str, input()))
	if(len(date)!=16 or len(date)!=10):
		print('ERROR')
	elif(len(date)==16):
		ToISO(date)
	else:
		ToDOSFAT(date)

except:
	sys.exit(0)