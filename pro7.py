import math
def main():
	n1=int(input())
	while(n1!=0):
		l=math.sqrt(n1)
		if l==int(l):
			print(int(l))
			break
		else:
			n1=n1-1
	if n1==0:
		print('no')
try:
  main()
except:
  print('invalid')
