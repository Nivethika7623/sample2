def f(s1,n1,m1):
	su=0
	while(True):
		su+=n1+m1
		if s1==su:
			return 'yes'
		if su>s1:
			break
	return 'no'
def main():
	n=int(input())
	a=int(input())
	b=int(input())
	print(f(n//2,a,b))
  
try:
  main()
except:
  print('invalid')
