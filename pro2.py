x1=int(input())
y1=int(input())
b1=str(x1)
l1=[]
for i in range(len(b1)):
    l1.append(b1[i])
for i in range(y1,len(b1)):
    print(int(l1[i]),end=' ')
