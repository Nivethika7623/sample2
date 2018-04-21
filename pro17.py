n=int(input())
l=[]
f=0
for i in range(n-1):
	l.append(int(input()))
k=int(input())
for i in range(n):
	if l[i]==l[i+1]:
		s1=l[i]+l[i+1]
		if s1==k:
			f=1
		print('yes')
if f!=1:
	  print('no')
