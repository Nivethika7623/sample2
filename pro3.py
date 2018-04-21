def g(a1,b1):
	k=0
	o=''
	c=0
	f=0
	for i in range(len(a1)):
		if len(a1)<len(b1):
			if a1[i]==b1[i]:
				o+=a1[i]
				k=k+1
		else :
			f=1
			break
	i=0
	if f==1:
		while(True):
			if a1[i]==b1[i]:
				o+=a1[i]
			else :
				o+=b1[i]
				c=c+1
			if i==3:
				break
			i=i+1
		return c

	for i in range(k,len(b1)):
		o+=b1[i]
		c=c+1
	return c
 
def main():
	a1=input()
	b1=input()
	print(g(a1,b1))
try:
 	 main()
except:
 	 print('invalid')
