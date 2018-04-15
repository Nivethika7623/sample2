N=int(input())
L=[]
F=0
for i in range(1,N//2+1):
	if N%i==0:
		L.append(i)
L.append(N)
for i in L:
	print(i)
