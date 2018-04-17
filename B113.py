def norep(l1,k1):
	c=0
	for i in l1:
		if k1==i:
			c=c+1
	return c
def main():
	try:
		n=int(input())
		k1=int(input())
		l1=[]
		for i in range(n):
			l1.append(int(input()))
		print(norep(l1,k1))
	except:
		print('invalid')
main()
