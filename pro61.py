def encode(str0,str2):
	(n1,n2)=(len(str0),len(str2))
	(enstr0,enstr2)=('','')
	for i in range(n1):
		c=ord(str0[i])
		c=c+10
		if c > 122:
			c=c-26
		enstr0+=chr(c)
	enstr2+=str2[0]
	for i in range(1,n2-1):
		c=ord(str2[i])
		c=c+10
		if c > 122:
			c=c-26
		enstr2+=chr(c)
	enstr2+=str2[n2-1]
	print(enstr0,enstr2)
def main():
	try:
		str0=input()
		str2=input()
		encode(str0,str2)
	except:
		print('invalid input')
main()
