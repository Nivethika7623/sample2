A=int(input())
l=[]
for i in range(2,100):
    B=1
    for j in range(2,i):
        if(i%j==0):
            B=0
            break
    if(B==1):
        l.append(i)
for i in range(0,len(l)):
    if(A%l[i]==0):
        print(l[i])
