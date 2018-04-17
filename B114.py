def kodd(l1,k1):
	c=0
	for i in range(len(l1)):
		if l1[i]%2!=0:
			c=c+1
			if c==k1:
				return l1[i]
	return 'none'
def main():
	try:
		n=int(input())
		k1=int(input())
		l1=[]
		for i in range(n):
			l1.append(int(input()))
		print(kodd(l1,k1))
	except:
		print('invalid')
main()
