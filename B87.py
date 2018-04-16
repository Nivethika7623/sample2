import sys
def gcd():
	(x,y)=map(int,sys.stdin.readline().split())
	while(y!=0):
		t=y
		y=x%y
		x=t
	print(x)
try:
	gcd()
except:
	print('invalid')
