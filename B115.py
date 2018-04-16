def small2(l1,k1):
	l1.sort()
	return l1[k1-1]
def main():
	try:
		n1=int(input())
		k1=int(input())
		l1=[]
		for i in range(n1):
			l1.append(int(input()))
		print(small2(l1,k1))
	except:
		print('invalid')
main()
