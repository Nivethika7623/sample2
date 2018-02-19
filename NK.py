N=int(input("N:"))
K=int(input("K:"))
M=[]
S=0
for i in range(0,N):
a=input()
M.append(a)
for i in range(0,K):
S=S+int(M[i])
print(S)
