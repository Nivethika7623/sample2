def fre(li):
	li.sort()
	rep=[]
	n=len(li)
	for i in range(1,n):
			if li[i]==li[i-1] :
				if li[i] in rep :
					continue
				rep.append(li[i])
	print(rep)

def main():
	try:
		li=[]
		n=int(input())
		for i in range(n):
			li.append(int(input()))
		fre(li)
	except:
		print('invalid')

main()
