def checkkn(l1,k1):
	if k1 in l1:
		return 'yes'
	return 'no'
def main():
	try:
		n=int(input())
		k1=int(input())
		l1=[]
		for i in range(n):
			l1.append(int(input()))
		print(checkkn(l1,k1))
	except:
		print('invalid')
main()
